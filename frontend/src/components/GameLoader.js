import React, { useEffect, useState } from 'react';
import { loadAssetsAsync } from '../utils/AssetManager';
import { log } from '../../utils/logger';

const GameLoader = ({ onAssetsLoaded }) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadAssets = async () => {
      try {
        log.info('Starting asset loading');
        await loadAssetsAsync();
        setLoading(false);
        onAssetsLoaded();
        log.info('Assets loaded successfully');
      } catch (err) {
        setError(err);
        log.error('Error loading assets: {}', err);
      }
    };

    loadAssets();
  }, [onAssetsLoaded]);

  if (error) {
    return <div>Error loading assets: {error.message}</div>;
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  return null;
};

export default GameLoader;