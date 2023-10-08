'use client'


import React, { useState, useEffect } from 'react';
import './cursorfollower.css';

const CursorFollower = () => {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [followerPosition, setFollowerPosition] = useState({ x: 0, y: 0 });
  const [isMoving, setIsMoving] = useState(false);
  const [rotation, setRotation] = useState(0);

  useEffect(() => {
    const handleMouseMove = (event) => {
      const { clientX, clientY } = event;
      setPosition({ x: clientX, y: clientY });
    };

    const handleMouseClick = (event) => {
      const { clientX, clientY } = event;
      setIsMoving(true);
      setPosition({ x: clientX, y: clientY });
    };

    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('click', handleMouseClick);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('click', handleMouseClick);
    };
  }, []);

  useEffect(() => {
    const lerp = (start, end, t) => {
      return start * (1 - t) + end * t;
    };

    const updateFollowerPosition = () => {
      setFollowerPosition((prevPosition) => {
        const lerpAmount = 0.05;
        const x = lerp(prevPosition.x, position.x, lerpAmount);
        const y = lerp(prevPosition.y, position.y, lerpAmount);

        const dx = x - prevPosition.x;
        const dy = y - prevPosition.y;
        const newRotation = Math.atan2(dy, dx) * (180 / Math.PI);
        setRotation(newRotation);

        return { x, y };
      });

      if (isMoving) {
        const distance = Math.sqrt(
          Math.pow(position.x - followerPosition.x, 2) + Math.pow(position.y - followerPosition.y, 2)
        );

        if (distance <= 1) {
          setIsMoving(false);
        }
      }
    };

    const animationFrame = requestAnimationFrame(updateFollowerPosition);

    return () => {
      cancelAnimationFrame(animationFrame);
    };
  }, [position, followerPosition, isMoving]);

  const cursorStyle = {
    left: followerPosition.x,
    top: followerPosition.y,
    transform: `translate(-50%, -50%) rotate(${rotation}deg)`,
  };

  return (
    <div className="cursor-follower" style={cursorStyle}>
      <img
        src="rocket.png"
        alt="Cursor Follower"
        className= "cursor-image"
      />
    </div>
  );
};

export default CursorFollower;