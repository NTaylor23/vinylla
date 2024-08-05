import { Release, Track } from "../compiler/types";

interface ReleaseModalProps {
  release: Release;
  isVisible: boolean;
  handleClose: () => void;
}
export const ReleaseModal = (props: ReleaseModalProps) => {
  if (!props.isVisible) {
    return null;
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-25 backdrop-blur-sm flex justify-center items-center">
      <div className="w-[400px]">
        <button
          className="text-white text-xl place-self-end"
          onClick={props.handleClose}
        >
          X
        </button>
        <img
          height="400"
          width="400"
          className="rounded-t-lg "
          src={props.release.image_url}
          alt=""
        />

        <div className="bg-white p-2 rounded">
          <div>
            <p className="mb-1 font-semibold text-slate-800">
              {props.release.formatted_name} - {props.release.album_title}
            </p>
          </div>
          <div className="px-2 py-1">
            <div className="mb-1 font-sm text-xs text-slate-800">
              {props.release.tracks.map((track: Track) => {
                return (
                  <ul key={track.track_title} className="list-none">
                    <div className="flex justify-between">
                      <span className="text-left font-mono">
                        {track.track_title}
                      </span>
                      <span className="text-left w-20 font-mono">
                        {track.duration}
                      </span>
                    </div>
                  </ul>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
