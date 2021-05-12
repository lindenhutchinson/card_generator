<template>
  <v-card
    style="margin: 0 auto"
    v-if="card"
    class="mx-auto card pb-2"
    :class="card.card_type.value"
    max-height="400"
    outlined
    raised
  >
    <v-list-item three-line>
      <v-list-item-content>
        <v-card-title class="headline card-title pl-2 pb-5 pt-2">{{
          card.game_type
        }}</v-card-title>

        <v-card flat class="card-text pt-2">
          <v-card-subtitle>
            <b>{{ card.game_text }}</b>
          </v-card-subtitle>
          <v-card-text class="pb-10">{{ card.game_info }}</v-card-text>

          <v-btn block @click="show_answer = true">Show Answer</v-btn>
          <v-expand-transition>
            <v-card
              raised
              justify="center"
              class="card-text v-card--reveal"
              v-if="show_answer"
            >
              <div class="answer-text pt-15">
                <p v-for="a in card.answer" v-bind:key="a[0]">
                  {{ a }}
                </p>
              </div>
              <div class="button">
                <v-btn text block @click="show_answer = false"> Close </v-btn>
              </div>
            </v-card>
          </v-expand-transition>
        </v-card>
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
      card_type: String,
    },
  },
  data() {
    return {
      show_answer: false,
    };
  },
  watch: {
    card: function () {
      this.show_answer = false;
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
.card-text {
  background: white;
}
.answer-text {
  text-align: center;
  vertical-align: middle;
}
.card {
  overflow: hidden;
}
.button {
  bottom: 0;
  position: absolute;
  width: 100%;
}
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>