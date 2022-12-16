cd ..
cd algos
for seed in 1 2 3 4
do
    python Off-PIAM_4x4.py   --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.01 --device cpu --exp-name Off-PIAM
    python Off-PIAM_10x10.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.015 --device cpu --exp-name Off-PIAM
    python Off-PIAM_16x16.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.02 --device cpu --exp-name Off-PIAM
    python Off-PIAM_24x24.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.03 --device cpu --exp-name Off-PIAM
done
