import { useState } from "react";
import { ReleaseModal } from "./ReleaseModal";
import { ReleaseCard } from "./ReleaseCard";
import { Release } from "../compiler/types";

interface ReleaseCardListProps {
  releases: Release[];
}

export const ReleaseCardList = (props: ReleaseCardListProps) => {
  const [showModal, setShowModal] = useState(false);
  const [activeId, setActiveId] = useState(0);

  const handleClick = (pk: number) => {
    setActiveId(pk)
    setShowModal(true);
  };

  const handleClose = () => {
    setActiveId(0);
    setShowModal(false);
  };

  const cards = props.releases.map((item: Release) => {
    return (
      <div key={item.pk}>
        <ReleaseCard release={item} handleClick={() => handleClick(item.pk)} />
      </div>
    );
  });
  return (
    <>
      <ReleaseModal
        release={
          props.releases.find((item: Release) => item.pk === activeId) ||
          props.releases[0]
        }
        isVisible={showModal}
        handleClose={handleClose}
      />
      <div className="grid grid-cols-7 gap-1">{cards}</div>
    </>
  );
};
