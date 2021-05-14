module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    host: '0.0.0.0',
    port: 3000
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/card_generator/'
    : '/',
}
