<template>
  <div class="game-feature">
    <!-- Core game features -->
    <FeatureA v-if="featureAEnabled" />
    <FeatureB v-if="featureBEnabled" />
    <!-- New feature parity components -->
    <MobileExclusiveFeature v-if="isMobile && mobileFeatureEnabled" />
    <WebExclusiveFeature v-if="!isMobile && webFeatureEnabled" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import FeatureA from './FeatureA.vue';
import FeatureB from './FeatureB.vue';
import MobileExclusiveFeature from './MobileExclusiveFeature.vue';
import WebExclusiveFeature from './WebExclusiveFeature.vue';

export default {
  components: {
    FeatureA,
    FeatureB,
    MobileExclusiveFeature,
    WebExclusiveFeature
  },
  computed: {
    ...mapState('gameFeatures', ['featureAEnabled', 'featureBEnabled', 'mobileFeatureEnabled', 'webFeatureEnabled', 'isMobile'])
  }
};
</script>

<style scoped>
.game-feature {
  /* Ensure responsive design */
  display: flex;
  flex-direction: column;
  padding: 10px;
}
</style>