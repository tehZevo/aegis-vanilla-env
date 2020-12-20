# Aegis "Vanilla" Environment Node
Runs Box2D and other OpenAI Gym environments as Aegis nodes

## Environment
* `ENV_NAME` - OpenAI Gym environment name to run
* `REWARD_URL` - Where to send step rewards
* `EPISODE_REWARD_URL` - Where to send episode rewards, defaults to `None`
* `ACTION_URL` - URL to pull actions from
* `PORT` - The port to listen on

## Notes
* The environment will be reset on its own. Currently, no information about resetting is available via any route.
