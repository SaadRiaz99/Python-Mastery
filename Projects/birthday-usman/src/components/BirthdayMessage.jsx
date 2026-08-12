import React, { useEffect, useState } from 'react';

const BirthdayMessage = () => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 500);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className={`birthday-message ${visible ? 'visible' : ''}`}>
      <div className="message-content">
        <p className="msg-eyebrow">HAPPY BIRTHDAY</p>
        <h1 className="msg-name">Usman Zafar</h1>
        <div className="msg-divider" aria-hidden="true">
          <span className="msg-tree">🌳</span>
          <span className="msg-cake">🎂</span>
        </div>
        <p className="msg-wish">
          “May your life keep growing like this tree —
          <br />
          stronger, higher, and more beautiful every day.”
        </p>
        <p className="msg-from">— From Saad Bin Riaz ❤️</p>
      </div>
    </div>
  );
};

export default BirthdayMessage;
