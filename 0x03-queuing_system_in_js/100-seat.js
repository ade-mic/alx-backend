import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// Create Redis client and connect to the server
const client = createClient();
client.connect().catch(err => console.error('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
}

// Initialize available seats and reservation status
reserveSeat(50);
let reservationEnabled = true;

// Create Kue queue
const queue = kue.createQueue();

// Create Express server
const app = express();
const port = 1245;

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat')
    .save((err) => {
      if (!err) {
        res.json({ status: 'Reservation in process' });
      } else {
        res.json({ status: 'Reservation failed' });
      }
    });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    await reserveSeat(currentSeats - 1);
    if (currentSeats - 1 === 0) {
      reservationEnabled = false;
    }
    done();
  });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
