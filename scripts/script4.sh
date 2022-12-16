cd ..
cd algos
for seed in 1 2 3 4
do
    python Penalty_4x4.py  --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.015 --invalid-action-penalty -0.01 --device cpu --exp-name Penalty
    python Penalty_10x10.py  --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.015 --invalid-action-penalty -0.01 --device cpu --exp-name Penalty
    python Penalty_16x16.py  --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.02 --invalid-action-penalty -0.01 --device cpu --exp-name Penalty
    python Penalty_24x24.py  --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.03 --invalid-action-penalty -0.01 --device cpu --exp-name Penalty
done
