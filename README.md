# Aegis "Vanilla" Environment Node
Runs Box2D and other OpenAI Gym environments as Aegis nodes

## Environment
* `ENV_NAME` - OpenAI Gym environment name to run (defaults to `LunarLanderContinuous-v2`)
* `EPISODE_REWARD` - additional reward given at end of episodes (defaults to 0)
* `PORT` - The port to listen on (defaults to 80)

## Notes
* The environment will be reset on its own.

## TODO
- support and document method for importing custom environments
- add route for resetting
- add route to return observation and action space types and shapes
