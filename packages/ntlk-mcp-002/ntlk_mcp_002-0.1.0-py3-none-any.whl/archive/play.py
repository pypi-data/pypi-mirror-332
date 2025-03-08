import textarena as ta

# Initialize agents
agents = {
    0: ta.agents.AnthropicAgent(model_name="claude-3-7-sonnet-latest"),
    1: ta.agents.AnthropicAgent(model_name="claude-3-5-haiku-latest"),
}

# Initialize environment from subset and wrap it
env = ta.make(env_id="SpellingBee-v0")
env = ta.wrappers.LLMObservationWrapper(env=env)
env = ta.wrappers.SimpleRenderWrapper(
    env=env,
    player_names={0: "claude-3-7-sonnet-latest", 1: "claude-3-5-haiku-latest"},
)

env.reset(num_players=len(agents))
done = False
while not done:
    player_id, observation = env.get_observation()
    action = agents[player_id](observation)
    done, info = env.step(action=action)
rewards = env.close()