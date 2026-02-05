const frameCache = new Map();

export const calculateFrame = (frame) => {
  if (frameCache.has(frame)) {
    return frameCache.get(frame);
  }
  // Simulating expensive calculation.
  const result = frame * Math.sin(frame) + frame * Math.cos(frame);
  frameCache.set(frame, result);
  return result;
};

export const clearFrameCache = () => {
  frameCache.clear();
};