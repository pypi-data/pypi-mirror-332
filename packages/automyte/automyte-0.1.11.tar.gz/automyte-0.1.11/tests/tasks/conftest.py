import pytest
import contextlib

from automyte.automaton.automaton import Automaton, Config
from automyte.automaton.types import FileTask
from automyte.discovery import ProjectExplorer, OSFile
from automyte.project import Project
from automyte.history.in_memory import InMemoryHistory
from automyte.vcs import VCS


class DummyExplorer(ProjectExplorer):
    def __init__(self) -> None:
        self.rootdir = 'smth'

    def get_rootdir(self) -> str:
        return self.rootdir

    def set_rootdir(self, newdir: str):
        self.rootdir = newdir
        return self.rootdir

    def flush(self):
        self.flushed = True

    def explore(self):
        yield OSFile(fullname=f"{self.rootdir}/hello.txt")


class DummyVCS(VCS):
    def run(self, *args):
        return

    @contextlib.contextmanager
    def preserve_state(self, config):
        self.preserve_state_called = True
        yield "newdir"


@pytest.fixture
def dummy_explorer():
    def _explorer_factory():
        return DummyExplorer()

    return _explorer_factory

@pytest.fixture
def dummy_vcs():
    def _vcs_factory():
        return DummyVCS()

    return _vcs_factory

@pytest.fixture
def dummy_automaton():

    def _dummy_automaton_factory(
        name: str = 'auto',
        projects: list[Project] | None = None,
        tasks: list[FileTask] | None = None
    ):
        return Automaton(
            name=name,
            config=Config.get_default().set_vcs(dont_disrupt_prior_state=False),
            history=InMemoryHistory(),
            projects=projects or [],
            tasks=tasks or [],
        )

    return _dummy_automaton_factory
