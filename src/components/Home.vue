<template>
  <div>
    <v-container>
      <v-row justify="center" no-gutters>
        <v-col sm="3" md="3" lg="2">
          <h3 class="ml-3 pt-3">Card Type</h3>
          <card-type-selector :card_type.sync="card_type" />
        </v-col>
        <v-col sm="3" md="3" lg="2">
          <h3 class="ml-3 pt-3">Game Type</h3>
          <game-type-selector
            :card_type="card_type"
            :game_type.sync="game_type"
          />
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col xs="4" sm="6" md="6" lg="4">
          <v-btn
            block
            :class="comp_type.value"
            :color="comp_type.colour"
            @click="get_card()"
          >
            Get Random Card
          </v-btn>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col xs="4" sm="6" md="6" lg="4">
          <cranium-card
            justify="center"
            class="mb-10"
            v-if="card"
            :card_type="comp_type"
            :card="card"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import CardTypeSelector from "./CardTypeSelector.vue";
import GameTypeSelector from "./GameTypeSelector.vue";
import CraniumCard from "./CraniumCard.vue";

import { get_random_card, get_type } from "../api";
export default {
  name: "Home",
  components: {
    CardTypeSelector,
    GameTypeSelector,
    CraniumCard,
  },
  data() {
    return {
      card: {},
      card_type: "random",
      game_type: "random",
    };
  },
  methods: {
    get_card: function () {
      this.card = get_random_card(this.card_type, this.game_type);
    },
  },
  computed: {
    comp_type: function () {
      return get_type(this.card_type);
    },
  },
};
</script>

<style scoped>
.star_performer {
  background: #4caf50;
}
.data_head {
  background: orangered;
}
.creative_cat {
  background: #2196f3;
}
.word_worm {
  background: #fbc02d;
}
.random {
  background: #a438b6;

  color: white;
}
</style>
