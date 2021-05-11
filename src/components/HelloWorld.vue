<template>
  <div>
    <v-container>
      <v-row justify="center">
        <v-col sm="12" md="3">
          <v-card-title>Card Type</v-card-title>
          <card-type-selector :card_type.sync="card_type" />
        </v-col>
        <v-col sm="12" md="3">
          <v-card-title>Card Game</v-card-title>
          <game-type-selector
            :card_type="card_type"
            :game_type.sync="game_type"
          />
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-btn block class="mb-5" color="primary" @click="get_card()">
          Get Random Card
        </v-btn>
      </v-row>

      <cranium-card v-if="card.answer" :card="card" />
    </v-container>
  </div>
</template>

<script>
import CardTypeSelector from "./CardTypeSelector.vue";
import GameTypeSelector from "./GameTypeSelector.vue";
import CraniumCard from "./CraniumCard.vue";

import { get_random_card } from "../api";
export default {
  name: "HelloWorld",
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
  mounted() {
    this.get_card();
  },
};
</script>
