# AnotherTake
A UGAHacks project which allows you to play around with audio effects using just your voice!

## Team
Sumedh Garimella, Georgia Institute of Technology

Parker Arneson, Denmark High School

Noah Sivinski, University of Georgia

Lucas Zhang, Georgia Institute of Technology

## Inspiration

Sumedh's a musician (Fly Montag on all streaming platforms!), and he has worked with Whatsapp chatbots on Twilio before for PennApps and for work with a nonprofit delivering remote healthcare to Guatemala, so he wanted to learn how to use Twilio's Programmable SMS for audio files. He also thinks it could be used to teach audio tech to people affordably (studio equipment and audio plugins can sometimes cost up to $100 on Splice!), and for musicians to experiment with ideas while they're not able to access their studios or equipment. 

## What it does

When a user sends a voice memo to the chatbot, the Twilio endpoint feeds the data to a Google Cloud Platform Cloud Function which not only extracts the data, but also converts it to a compatible file, and then reverses the file and returns it to the user. 

## How we built it

Twilio (for the phone endpoint and for keeping up contact with the user)
Google Cloud Platform Cloud Functions (for the backend)
Python
Scipy and Numpy do the manipulation of audio files

## Branches
main
bot (for backend development, runs in GCP, not from here)
demo (for the Github Pages site)

## Github Challenge things:
We did Github Pages, this readme, attempted to do a CODEOWNERS file, had multiple branches, and set up a rudimentary PR system. 

## Challenges we ran into

First off, there was no easy way to send an audio message to Twilio and easily access the metadata, and we knew people probably wouldn't call the number for an audio effect (although that might have been easier to use and could have been worth a try), so we eventually figured out how to send a voice message and parse it on the other side. We also had a lot of issues using the cloud function and converting from .amr (which is what voice memos on Android are encoded in) to .wav (which scipy and numpy use for audio processing), which stunted our ability to do more cooler effects such as delay, adding a beat, reverb, and even a vocoder. 

## Accomplishments that we're proud of

Two of our teammates had never done a hackathon before, and one was even a high schooler (Parker). He learned how to use Bootstrap and even learned how to reverse an audio file from Sumedh. 

Sumedh had never gotten a Twilio chatbot to accept an audio file as input before or successfully configured a Cloud Function before in his many hackathons, so these moments were victories he was very thrilled about!

## What we learned

We learned a lot about Twilio's functionalities, Cloud Functions, and working with audio files in general. Parker learned a lot about hackathons and how to make a quick project in his first-ever hackathon, and he hopes it will propel him to do even more when he gets to college. 

## What's next for AnotherTake

We realized that Twilio for audio was a pain to work with without calling or using prerecorded audio, neither of which would really make sense for our use case. As such, Sumedh will probably continue this project on his own and make it a web or mobile-based project instead of a Twilio bot due to the frustrations he had with setting that up. 

## Explanation of Domain.com submission:
letsdoanother.tech is a play on the saying "let's do another take", which you might hear in a recording studio!

