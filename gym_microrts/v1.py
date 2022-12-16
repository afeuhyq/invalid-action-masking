from .types import Config
import numpy as np

"""
WinLossRewardFunction(), 
ResourceGatherRewardFunction(),  
ProduceWorkerRewardFunction(),
ProduceBuildingRewardFunction(),
AttackRewardFunction(),
ProduceCombatUnitRewardFunction(),
CloserToEnemyBaseRewardFunction(),
reward_weight corresponds to above
"""
def randomAI():
    from ai import RandomBiasedSingleUnitAI
    return RandomBiasedSingleUnitAI()

def passiveAI():
    from ai import PassiveAI
    return PassiveAI()

shaped_reward_envs = True
hrl_envs = True

envs = []
envs += [dict(
    id=f"MicrortsMining-v1",
    entry_point='gym_microrts.envs:GlobalAgentMiningEnv',
    kwargs={'config': Config(
        frame_skip=9,
        ai2=passiveAI,
        map_path="maps/10x10/basesWorkers10x10.xml",
        microrts_path="~/microrts"
    )},
    max_episode_steps=200,
)]
envs += [dict(
    id=f"MicrortsProduceWorker-v1",
    entry_point='gym_microrts.envs:GlobalAgentProduceWorkerEnv',
    kwargs={'config': Config(
        frame_skip=9,
        ai2=passiveAI,
        map_path="maps/10x10/basesWorkers10x10.xml",
        microrts_path="~/microrts"
    )},
    max_episode_steps=200,
)]

envs += [dict(
    id=f"MicrortsAttackSparseReward-v1",
    entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
    kwargs={'config': Config(
        frame_skip=9,
        ai2=passiveAI,
        map_path="maps/10x10/basesWorkers10x10.xml",
        microrts_path="~/microrts",
        reward_weight=np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0])
    )},
    max_episode_steps=200,
)]
if shaped_reward_envs:
    envs += [dict(
        id=f"MicrortsAttackShapedReward-v1",
        entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            reward_weight=np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0])
        )},
        max_episode_steps=400,
    )]
if hrl_envs:
    envs += [dict(
        id=f"MicrortsAttackHRL-v1",
        entry_point='gym_microrts.envs:GlobalAgentHRLEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            hrl_reward_weights=np.array([
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
            ])
        )},
        max_episode_steps=200,
    )]

envs += [dict(
    id=f"MicrortsProduceCombatUnitsSparseReward-v1",
    entry_point='gym_microrts.envs:GlobalAgentProduceCombatUnitEnv',
    kwargs={'config': Config(
        frame_skip=9,
        ai2=passiveAI,
        map_path="maps/10x10/basesWorkers10x10.xml",
        microrts_path="~/microrts"
    )},
    max_episode_steps=400,
)]
if shaped_reward_envs:
    envs += [dict(
        id=f"MicrortsProduceCombatUnitsShapedReward-v1",
        entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            reward_weight=np.array([0.0, 1.0, 0.0, 1.0, 0.0, 7.0, 0.0])
        )},
        max_episode_steps=400,
    )]
if hrl_envs:
    envs += [dict(
        id=f"MicrortsProduceCombatUnitHRL-v1",
        entry_point='gym_microrts.envs:GlobalAgentHRLEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            hrl_reward_weights=np.array([
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0, 1.0, 0.0, 7.0, 0.0],
            ])
        )},
        max_episode_steps=400,
    )]


envs += [dict(
    id="MicrortsRandomEnemySparseReward-v1",
    entry_point='gym_microrts.envs:GlobalAgentBinaryEnv',
    kwargs={'config': Config(
        frame_skip=9,
        ai2=randomAI,
        map_path="maps/10x10/basesWorkers10x10.xml",
        microrts_path="~/microrts"
    )},
    max_episode_steps=600,
)]
if shaped_reward_envs:
    envs += [dict(
        id=f"MicrortsRandomEnemyShapedReward1-v1",
        entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=randomAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            reward_weight=np.array([0.0, 1.0, 0.0, 1.0, 1.0, 7.0, 0.0])
        )},
        max_episode_steps=600,
    )]
    envs += [dict(
        id=f"MicrortsRandomEnemyShapedReward2-v1",
        entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=randomAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            reward_weight=np.array([0.0, 1.0, 0.0, 1.0, 0.0, 7.0, 0.0])
        )},
        max_episode_steps=600,
    )]
    envs += [dict(
        id=f"MicrortsRandomEnemyShapedReward3-v1",
        entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=randomAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            reward_weight=np.array([5.0, 1.0, 1.0, 0.2, 1.0, 7.0, 0.2])
        )},
        max_episode_steps=600,
    )]
if hrl_envs:
    envs += [dict(
        id=f"MicrortsRandomEnemyHRL1-v1",
        entry_point='gym_microrts.envs:GlobalAgentHRLEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            hrl_reward_weights=np.array([
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 1.0, 1.0, 7.0, 0.0],
            ])
        )},
        max_episode_steps=600,
    )]
    envs += [dict(
        id=f"MicrortsRandomEnemyHRL2-v1",
        entry_point='gym_microrts.envs:GlobalAgentHRLEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            hrl_reward_weights=np.array([
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 1.0, 0.0, 7.0, 0.0],
            ])
        )},
        max_episode_steps=600,
    )]
    envs += [dict(
        id=f"MicrortsRandomEnemyHRL3-v1",
        entry_point='gym_microrts.envs:GlobalAgentHRLEnv',
        kwargs={'config': Config(
            frame_skip=9,
            ai2=passiveAI,
            map_path="maps/10x10/basesWorkers10x10.xml",
            microrts_path="~/microrts",
            hrl_reward_weights=np.array([
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [5.0, 1.0, 1.0, 0.2, 1.0, 7.0, 0.2],
            ])
        )},
        max_episode_steps=600,
    )]


# envs += [dict(
#     id="MicrortsSparseRewardPassiveEnemy-v1",
#     entry_point='gym_microrts.envs:GlobalAgentBinaryEnv',
#     kwargs={'config': Config(
#         frame_skip=9,
#         ai2=passiveAI,
#         map_path="maps/10x10/basesWorkers10x10.xml",
#         microrts_path="~/microrts"
#     )},
#     max_episode_steps=600,
# )]
# if shaped_reward_envs:
#     envs += [dict(
#         id=f"MicrortsShapedReward1PassiveEnemy-v1",
#         entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
#         kwargs={'config': Config(
#             frame_skip=9,
#             ai2=passiveAI,
#             map_path="maps/10x10/basesWorkers10x10.xml",
#             microrts_path="~/microrts",
#             reward_weight=np.array([5.0, 1.0, 1.0, 0.2, 1.0, 7.0, 0.2])
#         )},
#         max_episode_steps=600,
#     )]
# envs += [dict(
#     id=f"MicrortsGlobalAgentHRLProduceCombatUnitPerfect10x10FrameSkip9-v1",
#     entry_point='gym_microrts.envs:GlobalAgentHRLProduceCombatUnitPerfectEnv',
#     kwargs={'config': Config(
#         frame_skip=9,
#         ai2=passiveAI,
#         map_path="maps/10x10/basesWorkers10x10.xml",
#         microrts_path="~/microrts"
#     )},
#     max_episode_steps=400,
# )]
# envs += [dict(
#     id=f"MicrortsCombinedReward10x10F9ProduceCombatUnitsRandomBiased-v1",
#     entry_point='gym_microrts.envs:GlobalAgentCombinedRewardEnv',
#     kwargs={'config': Config(
#         frame_skip=9,
#         ai2=randomAI,
#         map_path="maps/10x10/basesWorkers10x10.xml",
#         microrts_path="~/microrts",
#         reward_weight=np.array([0.0, 1.0, 0.0, 1.0, 0.0, 7.0, 0.0])
#     )},
#     max_episode_steps=600,
# )]