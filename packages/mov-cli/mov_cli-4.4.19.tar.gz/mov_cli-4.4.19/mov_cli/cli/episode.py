from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from ..media import Metadata
    from ..scraper import Scraper

from devgoldyutils import Colours

from .ui import prompt

from ..media import MetadataType
from ..utils import EpisodeSelector
from ..cache import Cache
from ..utils import what_platform
from ..logger import mov_cli_logger

def handle_episode(episode_string: Optional[str], scraper: Scraper, choice: Metadata, fzf_enabled: bool, continue_watching: bool) -> Optional[EpisodeSelector]:
    if choice.type == MetadataType.SINGLE:
        return EpisodeSelector()

    if continue_watching:
        cache = Cache(what_platform())

        cached_episode = cache.get_cache(str(choice.id))

        if cached_episode is not None:
            return EpisodeSelector(**cached_episode)

    metadata_episodes = scraper.scrape_episodes(choice)

    if episode_string is None:
        mov_cli_logger.info(f"Scraping episodes for '{Colours.CLAY.apply(choice.title)}'...")

        if metadata_episodes.get(None) == 1:
            return EpisodeSelector()

        season = prompt(
            "Select Season", 
            choices = [season for season in metadata_episodes], 
            display = lambda x: f"Season {x}", 
            fzf_enabled = fzf_enabled
        )

        if season is None:
            return None

        episode = prompt(
            "Select Episode", 
            choices = [episode for episode in range(1, metadata_episodes[season] + 1)], 
            display = lambda x: f"Episode {x}",
            fzf_enabled = fzf_enabled
        )

        if episode is None:
            return None

        return EpisodeSelector(episode, season)

    try:
        episode_season = episode_string.split(":")

        episode = 1
        season = 1

        if len(episode_season) == 1 or episode_season[1] == "":
            episode = int(episode_season[0])

        elif len(episode_season) == 2:
            episode = int(episode_season[0])
            season = int(episode_season[1])

    except ValueError as e:
        mov_cli_logger.error(
            "Incorrect episode format! This is how it's done --> '5:1' (5 being episode and 1 being season)\n" \
                f"Error: {e}"
        )

        return None

    return EpisodeSelector(episode, season)