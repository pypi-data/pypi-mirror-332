# 23.11.24

from typing import Dict, Any, List, Union, List, Optional


class Episode:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

        self.id: int = data.get('id', 0)
        self.number: int = data.get('number', 1)
        self.name: str = data.get('name', '')
        self.duration: int = data.get('duration', 0)

    def __str__(self):
        return f"Episode(id={self.id}, number={self.number}, name='{self.name}', duration={self.duration} sec)"

class EpisodeManager:
    def __init__(self):
        self.episodes: List[Episode] = []

    def add(self, episode_data: Dict[str, Any]):
        """
        Add a new episode to the manager.

        Parameters:
            - episode_data (Dict[str, Any]): A dictionary containing data for the new episode.
        """
        episode = Episode(episode_data)
        self.episodes.append(episode)

    def get(self, index: int) -> Episode:
        """
        Retrieve an episode by its index in the episodes list.

        Parameters:
            - index (int): The zero-based index of the episode to retrieve.

        Returns:
            Episode: The Episode object at the specified index.
        """
        return self.episodes[index]
    
    def length(self) -> int:
        """
        Get the number of episodes in the manager.

        Returns:
            int: Number of episodes.
        """
        return len(self.episodes)
    
    def clear(self) -> None:
        """
        This method clears the episodes list.

        Parameters:
            - self: The object instance.
        """
        self.episodes.clear()

    def __str__(self):
        return f"EpisodeManager(num_episodes={len(self.episodes)})"


class SeasonData:
    def __init__(self, data: Dict[str, Any]):
        self.id: int = data.get('id', 0)
        self.number: int = data.get('number', 0)

    def __str__(self):
        return f"SeasonData(id={self.id}, number={self.number}, name='{self.name}'"

class SeasonManager:
    def __init__(self):
        self.seasons: List[SeasonData] = []
    
    def add_season(self, season_data):
        season = SeasonData(season_data)
        self.seasons.append(season)
        
    def get_season_by_number(self, number: int) -> Optional[Dict]:
        return self.seasons[number]

class Season:
    def __init__(self, season_data: Dict[str, Union[int, str, None]]):
        self.season_data = season_data

        self.id: int = season_data.get('id', 0)
        self.number: int = season_data.get('number', 0)
        self.name: str = season_data.get('name', '')
        self.slug: str = season_data.get('slug', '')
        self.type: str = season_data.get('type', '')
        self.seasons_count: int = season_data.get('seasons_count', 0)
        
        self.episodes: EpisodeManager = EpisodeManager()

        self.seasonsData: SeasonManager = SeasonManager()
        for element in season_data['seasons']:
            self.seasonsData.add_season(element)
        

class Stream:
    def __init__(self, name: str, url: str, active: bool):
        self.name = name
        self.url = url
        self.active = active

    def __repr__(self):
        return f"Stream(name={self.name!r}, url={self.url!r}, active={self.active!r})"

class StreamsCollection:
    def __init__(self, streams: list):
        self.streams = [Stream(**stream) for stream in streams]

    def __repr__(self):
        return f"StreamsCollection(streams={self.streams})"

    def add_stream(self, name: str, url: str, active: bool):
        self.streams.append(Stream(name, url, active))

    def get_streams(self):
        return self.streams

    
class WindowVideo:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.id: int = data.get('id', '')
        self.name: str = data.get('name', '')
        self.filename: str = data.get('filename', '')
        self.size: str = data.get('size', '')
        self.quality: str = data.get('quality', '')
        self.duration: str = data.get('duration', '')
        self.views: int = data.get('views', '')
        self.is_viewable: bool = data.get('is_viewable', '')
        self.status: str = data.get('status', '')
        self.fps: float = data.get('fps', '')
        self.legacy: bool = data.get('legacy', '')
        self.folder_id: int = data.get('folder_id', '')
        self.created_at_diff: str = data.get('created_at_diff', '')

    def __str__(self):
        return f"WindowVideo(id={self.id}, name='{self.name}', filename='{self.filename}', size='{self.size}', quality='{self.quality}', duration='{self.duration}', views={self.views}, is_viewable={self.is_viewable}, status='{self.status}', fps={self.fps}, legacy={self.legacy}, folder_id={self.folder_id}, created_at_diff='{self.created_at_diff}')"

class WindowParameter:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        params = data.get('params', {})
        self.token: str = params.get('token', '')
        self.expires: str = str(params.get('expires', ''))
        self.url = data.get('url')

    def __str__(self):
        return (f"WindowParameter(token='{self.token}', expires='{self.expires}', url='{self.url}', data={self.data})")