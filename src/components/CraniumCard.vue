<template>
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
          {{ card.game_type }}
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
</template>



<script>

export default {
  name: "CraniumCard",
  props: {
    card: {
      game_text: String,
      answer: String,
      game_type: String,
      game_info: String,
    },
  },
  data() {
    return {
      show_answer: false,
    };
  },
};
</script>