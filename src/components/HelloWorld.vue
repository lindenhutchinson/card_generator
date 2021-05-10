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

      <v-card
        style="margin: 0 auto"
        v-if="card"
        class="mx-auto"
        max-width="800"
        outlined
      >
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Random Card</div>
            <v-card-text> </v-card-text>
            <v-list-item-title class="headline mb-1">
              {{ card.card_game }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ card.game_info }}</v-list-item-subtitle>
            <v-card-text>
              {{ card.game_text }}
            </v-card-text>
            <v-btn max-width="150" @click="show_answer = !show_answer"
              >Show Answer</v-btn
            >
            <v-card-text v-if="show_answer">
              {{ card.answer }}
            </v-card-text>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import CardTypeSelector from "./CardTypeSelector.vue";
import GameTypeSelector from "./GameTypeSelector.vue";
import { get_random_card } from "../api";
export default {
  name: "HelloWorld",
  components: {
    CardTypeSelector,
    GameTypeSelector,
  },
  props: {
    msg: String,
  },
  data() {
    return {
      card: {},
      show_answer: false,
      games: [],
      card_type: "random",
      game_type: "random",

      // TODO: define card types as an enum
      //        define card games as enums
    };
  },
  methods: {
    get_card: function () {
      this.show_answer = false;
      this.card = get_random_card(this.card_type, this.game_type);
    },
  },
  mounted() {
    this.get_card();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
