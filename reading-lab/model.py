"""Generated from uml/02_classes.puml by generate.py."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol


@dataclass
class ReadingSession:
    child_id: str
    task: ReadingTask
    phase: Phase
    audio_ref: str | None
    seconds: float
    transcript: str | None
    answers: list[int]
    result: Assessment | None


@dataclass
class ReadingTask:
    text: str
    questions: list[Question]


@dataclass
class Question:
    prompt: str
    options: list[str]
    key: int


@dataclass
class Assessment:
    word_edits: int
    reference_words: int
    words_per_minute: float
    correct: int
    total: int


class Phase(Enum):
    ASSIGNED = "ASSIGNED"
    RECORDING = "RECORDING"
    RECOGNIZING = "RECOGNIZING"
    REVIEW = "REVIEW"
    QUESTIONS = "QUESTIONS"
    COMPLETED = "COMPLETED"


class Recognizer(Protocol):
    def transcribe(self, audio_ref: str) -> str: ...


class Scorer(Protocol):
    def evaluate(self, session: ReadingSession) -> Assessment: ...
