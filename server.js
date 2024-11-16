const express = require('express');
const app = express();
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/synerga', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const moodSchema = new mongoose.Schema({
  mood: String,
  timestamp: Date,
});

const Mood = mongoose.model('Mood', moodSchema);

app.use(express.json());

app.post('/trackMood', async (req, res) => {
  try {
    const mood = req.body.mood;
    const newMood = new Mood({ mood, timestamp: new Date() });
    await newMood.save();
    res.json({ message: 'Mood tracked successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error tracking mood' });
  }
});

app.get('/moodHistory', async (req, res) => {
  try {
    const moodHistory = await Mood.find().sort({ timestamp: -1 });
    res.json(moodHistory);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error retrieving mood history' });
  }
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
