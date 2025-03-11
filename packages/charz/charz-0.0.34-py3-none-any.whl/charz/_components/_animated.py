from __future__ import annotations

from functools import wraps
from copy import deepcopy
from typing import Any, ClassVar

from typing_extensions import Self

from .._animation import AnimationSet, Animation
from .._annotations import AnimatedNode


# TODO: add `.play_backwards` attribute or method
# TODO: ensure last frame was rendered before `.is_playing = False`,
#       because a loop checking if it should replay the animations will
#       reset it back to the first frame before the last one is displayed
class Animated:  # Component (mixin class)
    animated_instances: ClassVar[dict[int, AnimatedNode]] = {}

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        instance = super().__new__(cls, *args, **kwargs)
        Animated.animated_instances[instance.uid] = instance  # type: ignore
        if (class_animations := getattr(instance, "animations", None)) is not None:
            instance.animations = deepcopy(class_animations)
        else:
            instance.animations = AnimationSet()

        # inject `._wrapped_update_animated()` into `.update()`
        def update_method_factory(instance: AnimatedNode, bound_update):  # noqa: ANN001 ANN202
            @wraps(bound_update)
            def new_update_method(delta: float) -> None:
                bound_update(delta)  # TODO: swap order will fix rendering??
                instance._wrapped_update_animated(delta)

            return new_update_method

        instance.update = update_method_factory(instance, instance.update)  # type: ignore
        return instance  # type: ignore

    animations: AnimationSet
    current_animation: Animation | None = None
    is_playing: bool = False
    _frame_index: int = 0

    def with_animations(self, /, **animations: Animation) -> Self:
        for animation_name, animation in animations.items():
            setattr(self.animations, animation_name, animation)
        return self

    def with_animation(
        self,
        animation_name: str,
        animation: Animation,
        /,
    ) -> Self:
        self.add_animation(animation_name, animation)
        return self

    def add_animation(
        self,
        animation_name: str,
        animation: Animation,
        /,
    ) -> None:
        setattr(self.animations, animation_name, animation)

    def play(self, animation_name: str, /) -> None:
        self.current_animation = getattr(self.animations, animation_name, None)
        self.is_playing = True
        self._frame_index = 0
        # the actual logic of playing the animation is handled in `.update(...)`

    def _wrapped_update_animated(self, _delta: float) -> None:
        if self.current_animation is None:
            self.is_playing = False
            return
        self.texture = self.current_animation.frames[self._frame_index]
        frame_count = len(self.current_animation.frames)
        self._frame_index = min(self._frame_index + 1, frame_count - 1)
        if self._frame_index == frame_count - 1:
            self.is_playing = False

    def _free(self) -> None:
        del Animated.animated_instances[self.uid]  # type: ignore
        super()._free()  # type: ignore
