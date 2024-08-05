import { Release } from "../compiler/types";

interface ReleaseCardProps {
  release: Release;
  handleClick: () => void;
}

export const ReleaseCard = (props: ReleaseCardProps) => {
  return (
    <div className="w-auto m-2 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 ">
      <img
        height="240"
        width="240"
        className="rounded-t-lg "
        src={props.release.image_url}
        alt=""
        onClick={props.handleClick}
      />
      <div className="px-2 py-1">
        <h5 className="mb-1 text-1xl font-bold tracking-tight text-gray-900 dark:text-white">
          {props.release.album_title}
        </h5>
        <p className="mb-1 font-normal text-slate-50">
          {props.release.formatted_name}
        </p>
        <p className="mb-1 font-normal text-sm text-slate-400">
          {props.release.genre} - {props.release.style}
        </p>
        <p className="mb-1 font-sm text-xs text-gray-700 dark:text-gray-400">
          {props.release.year > 0 ? props.release.year : ""}
        </p>
      </div>
    </div>
  );
};
