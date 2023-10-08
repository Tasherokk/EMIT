import React from 'react';

function EpithetPopup({ epitet, onClose }) {
  return (
    <div className="epithet-popup">
      <div className="popup-content">
        <p>{epitet}</p>
        <button onClick={onClose}>Закрыть</button>
      </div>
    </div>
  );
}

export default EpithetPopup;
