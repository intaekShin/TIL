const app = new Vue({
  delimiters: ['[[', ']]'],
  el: "#app",
  data: {
    logo: 'MO<i class="fab fa-vuejs"></i>IE',
    isMain: true,
    genres: [],
    movies: [],
    search: '', // 검색 기능을 구현할 때, 사용자의 입력 값을 이곳에 쌍방향 바인딩 합니다.

    detailView: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
    movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
  },
  methods: {
    toggleDetail: function(id=null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
      if (id) {
        const movie = this.movies[0]  // 현재는 무조건 $data.movies 의 첫 번째 영화를 선택합니다. 실제로는 인자로 넘어온 id 를 통해 특정 영화를 찾습니다.

        // Better way..?
        this.movieDetail.title = movie.title
        this.movieDetail.audience= movie.audience
        this.movieDetail.poster_url= movie.poster_url
        this.movieDetail.description = movie.description

        this.movieDetail.scores = []  // 상세 페이지에서 표시할 모든 $data.scores 를 받아와야 합니다.
        this.movieDetail.genre = '' // 해당 movie 의 genreId 를 통해 genre.name 을 찾아서 저장합니다.
      }
      this.detailView = !this.detailView
    },
  },
  computed: {},

  watch: {},

  created: function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, API 서버에서 장르목록만 받아옵니다.
      axios.get(`/api/v1/genres`)  // 만약 API 서버를 사용하지 않거나 서버가 꺼져있다면 에러가 발생합니다.
        .then(res => this.genres = res.data)
      axios.get(`/api/v1/movies`)
        .then(res => this.movies = res.data)
  }
});
