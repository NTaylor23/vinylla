export interface Release {
  pk: number;
  artist_name: string;
  formatted_name: string;
  album_title: string;
  genre: string;
  style: string;
  format: string;
  discogs_release_id: number;
  year: number;
  price: number;
  in_wantlist: boolean;
  image_url: string;
  thumbnail_url: string;
  tracks: Track[]
}

export interface Track {
  track_title: string;
  duration: string;
}
