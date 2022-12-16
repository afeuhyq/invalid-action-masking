cd ..
cd algos
for seed in 1 2 3 4
do
    python CO-IAM_4x4.py   --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.0 --device cpu --exp-name CO-IAM
    python CO-IAM_10x10.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.0 --device cpu --exp-name CO-IAM
    python CO-IAM_16x16.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.0 --device cpu --exp-name CO-IAM
    python CO-IAM_24x24.py --seed $seed --total-timesteps 1000000 --prod-mode --wandb-project-name invalid-action-masking --capture-video --ent-coef 0.0 --device cpu --exp-name CO-IAM
done
