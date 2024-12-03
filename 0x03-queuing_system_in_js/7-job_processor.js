import kue from 'kue';

// Create an array that will contain the blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function sendNotification
function sendNotification(phoneNumber, message, job, done) {
  // Track the progress of the job of 0 out of 100

  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an Error object
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track the progress to 50%
  job.progress(50, 100);

  // Log to the console
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs in the queue push_notification_code_2 with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
})