interface configObject {
  host: string;
  env: string;
  port: number;
}

const configValidator = (config: configObject) => {
  const requiredProps = [
    'host',
    'env',
    'port',
  ]

  for (let i = 0; i < requiredProps.length; i++) {
    if (!config.hasOwnProperty(requiredProps[i])) {
      return false;
    }
  }

  if (typeof config.port !== 'number' || (config.port < 0 || config.port > 65_535)) {
    return false;
  }

  return true;
}

//need to check if 'host' 'port' and 'env' are on the object inputed.
//going to assume valid port just means possible, 0-63,535 int.

const tests = [
  {
    host: 'localhost',
    env: 'yourmom',
    port: 420
  },
  {
    env: 'yourmom',
    port: 420
  },
  {
    host: 'localhost',
    port: 420
  },
  {
    host: 'localhost',
    env: 'yourmom',
    port: 100_000
  },
  {
    host: 'localhost',
    env: 'yourmom',
    port: -1
  },
  {
    host: 'localhost',
    env: 'yourmom',
  },
]

const tester = () => {
  for (let test of tests) {
    let result = configValidator(test)
    console.log(`${JSON.stringify(test)}\n${result}`)
  }
}

tester()