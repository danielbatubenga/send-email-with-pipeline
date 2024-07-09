import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 10000 } // Simula 1000 requisições por segundo por 1 minuto
  ],
};

export default function () {
  let res = http.get('http://localhost:3000/');
  sleep(1);
}
