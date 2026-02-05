import React, { useEffect, useRef } from 'react';
import { calculateFrame } from '../utils/AnimationUtils';
import { logPerformance } from '../utils/PerformanceMonitor';

const AnimationManager = ({ animations }) => {
  const frameRef = useRef(0);
  const requestIdRef = useRef(null);
  
  useEffect(() => {
    const renderFrame = () => {
      frameRef.current = calculateFrame(frameRef.current);
      requestIdRef.current = requestAnimationFrame(renderFrame);
    };
    
    logPerformance('Animation Start');
    requestIdRef.current = requestAnimationFrame(renderFrame);

    return () => {
      cancelAnimationFrame(requestIdRef.current);
      logPerformance('Animation Stop');
    };
  }, [animations]);
  
  return (
    <div className="animation-container">
      {animations.map(animation => (
        <div key={animation.id} className="animation-item" style={animation.style} />
      ))}
    </div>
  );
};

export default AnimationManager;