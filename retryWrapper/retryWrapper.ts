import { setTimeout as wait } from 'timers/promises';

const clientID = 'xxxxxx'
const clientSecret = 'xxxxxxx'
//^^^remember to change this on twitch after you are done!!!
//replacing them with junk for now

const tokenRequestData = {
  client_id: clientID,
  client_secret: clientSecret,
  grant_type: 'client_credentials',
}

const fetchWithRetry = async (url: string, maxRetries: number) => {
  const tokenPromise = await fetch(
    `https://id.twitch.tv/oauth2/token?client_id=${clientID}&client_secret=${clientSecret}&grant_type=client_credentials`,
    { method: 'POST',
      // headers: {
      //   'client_id': clientID,
      //   'client_secret': clientSecret,
      //   'grant_type': 'client_credentials'
      // },
      // body: JSON.stringify(tokenRequestData),
    })
  const tokenJson = await tokenPromise.json()
  // console.log(tokenJson)
  const token = tokenJson.access_token
  // console.log(`token: ${token}`)
  
  for (let i = 0; i < maxRetries; i++) {
    console.log(`attempt number: ${i}`)
    const requestAttempt = await fetch(
      url,
      { method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Client-ID': clientID,
          'Authorization': 'Bearer ' + token,
        },
        body: 'fields name;'
      }
    )
    if (requestAttempt.ok) {
      console.log('success!')
      const result = await requestAttempt.json()
      return result
    } else {
      console.log(requestAttempt.status)
    }
    wait(300);
  }
  return `failed to connect after ${maxRetries} attempts`
  //okay that's auth taken care of.
  //now we need to set up a loop with a timer that iterates maxRetries times
  //and terminates if it succeeds.
  //we can test if it works by giving it an object ID that doesn't exist maybe?
  //can test in postman.
}

//write a fn that calls an API, retries up to x times on failure, with a short delay between attempts.
//use fetch and async-await

const result = await fetchWithRetry('https://api.igdb.com/v4/games', 3)
console.log(result)