import axios from 'axios'
import getCookie from "./getCookie";

axios.defaults.xsrfHeaderName = 'x-csrftoken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true

let djangoURL = 'http://127.0.0.1:8000'
let defaultTimeout = 30000
//if (process.env.PROD) {
//  djangoURL = 'https://##.##.#.##:###'
//  defaultTimeout = 10000
//}
axios.defaults.baseURL = djangoURL
axios.defaults.timeout = defaultTimeout

if(!getCookie(import.meta.env.VITE_CSRF_RX)) {
  axios.get("http://localhost:8000/get-csrf");
}

const api = axios.create()
export { api };
