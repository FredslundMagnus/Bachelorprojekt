
# Parameters

    Name :                      Lights2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      51400798867 function calls (49806777385 primitive calls) in 258900.72 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.723 258900.723 {built-in method builtins.exec}
                      1    0.379    0.379 258900.723 258900.723 <string>:1(<module>)
                      1 5892.482 5892.482 258900.343 258900.343 optionCritic.py:195(option_critic_run)
        2105495090/518843465 9801.220    0.000 109956.527    0.000 module.py:866(_call_impl)
               56686375 8971.602    0.000 109624.452    0.002 optionCritic.py:143(actor_loss_fn)
              176294625  799.594    0.000 102545.756    0.001 optionCritic.py:70(get_state)
              176294625 2267.907    0.000 99347.990    0.001 container.py:117(forward)
                2267455   18.876    0.000 80154.359    0.035 tensor.py:195(backward)
                2267455   25.703    0.000 80135.163    0.035 __init__.py:68(backward)
                2267455 80056.400    0.035 80056.400    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              352589250  921.221    0.000 63566.669    0.000 conv.py:398(forward)
              352589250  529.412    0.000 62271.644    0.000 conv.py:390(_conv_forward)
              352589250 61742.232    0.000 61742.232    0.000 {built-in method conv2d}
               56686375 3471.534    0.000 20331.279    0.000 optionCritic.py:91(get_action)
              695138090 1588.455    0.000 20064.225    0.000 linear.py:93(forward)
              695138090  644.064    0.000 17811.001    0.000 functional.py:1737(linear)
              695138090 17022.924    0.000 17022.924    0.000 {built-in method torch._C._nn.linear}
               56686375 1171.100    0.000 13482.408    0.000 optionCritic.py:80(predict_option_termination)
              113372750 1226.030    0.000 7791.689    0.000 distribution.py:34(__init__)
              528883875  509.213    0.000 7228.457    0.000 activation.py:713(forward)
               56686375  570.167    0.000 6732.553    0.000 categorical.py:115(log_prob)
              528883875  548.456    0.000 6719.244    0.000 functional.py:1364(leaky_relu)
              528883875 6063.258    0.000 6063.258    0.000 {built-in method torch._C._nn.leaky_relu}
               56686375  770.701    0.000 5729.494    0.000 categorical.py:49(__init__)
              171922852  375.563    0.000 5445.662    0.000 optionCritic.py:77(get_Q)
                2267455   52.917    0.000 5322.082    0.002 optimizer.py:84(wrapper)
               56686375  415.817    0.000 5252.666    0.000 bernoulli.py:34(__init__)
                2267455   27.218    0.000 5132.786    0.002 grad_mode.py:24(decorate_context)
                 566863   92.392    0.000 5084.378    0.009 optionCritic.py:116(critic_loss_fn)
                2267455  135.682    0.000 5053.285    0.002 rmsprop.py:56(step)
                2267455   13.923    0.000 4919.897    0.002 game.py:41(step)
                2267455  130.746    0.000 4771.315    0.002 _functional.py:203(rmsprop)
                2267455   20.471    0.000 4749.558    0.002 layers.py:718(step)
              113939613  394.917    0.000 4267.625    0.000 optionCritic.py:88(get_terminations)
               56686375 2352.449    0.000 3471.759    0.000 constraints.py:398(check)
                2267455   85.053    0.000 3011.150    0.001 layers.py:17(step)
               56686375  240.392    0.000 2918.167    0.000 layer.py:98(move)
               56686375  484.199    0.000 2735.311    0.000 distribution.py:240(_validate_sample)
              176294625  224.028    0.000 2045.980    0.000 activation.py:101(forward)
               56686375 1965.391    0.000 1965.391    0.000 constraints.py:364(check)
               31744364 1951.327    0.000 1951.327    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56686375  406.591    0.000 1947.470    0.000 bernoulli.py:86(sample)
               56686375  396.189    0.000 1871.199    0.000 layers.py:735(check)
               56686375  973.534    0.000 1852.989    0.000 categorical.py:123(entropy)
              176294625  202.600    0.000 1821.952    0.000 functional.py:1195(relu)
             2727965730 1777.143    0.000 1777.307    0.000 module.py:934(__getattr__)
               56686375 1762.063    0.000 1762.063    0.000 constraints.py:249(check)
                2267456  184.559    0.000 1709.122    0.001 layers.py:684(update)
              170059125  241.228    0.000 1681.264    0.000 utils.py:106(__get__)
              396804625 1612.401    0.000 1612.401    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              176294625  170.466    0.000 1599.092    0.000 flatten.py:39(forward)
              176294625 1590.787    0.000 1590.787    0.000 {built-in method relu}
              171192851  195.277    0.000 1521.779    0.000 tensor.py:525(__rsub__)
                 566863 1214.681    0.002 1463.475    0.003 replaybuffer.py:42(sample_option_critic)
              113372750  519.059    0.000 1458.042    0.000 functional.py:46(broadcast_tensors)
              176294625 1428.626    0.000 1428.626    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31744364 1396.589    0.000 1396.589    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24942005   55.959    0.000 1383.826    0.000 tensor.py:575(__iter__)
               56686375  373.776    0.000 1334.326    0.000 categorical.py:108(sample)
              171192851 1298.934    0.000 1298.934    0.000 {built-in method rsub}
               24942005 1292.876    0.000 1292.876    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56686375   67.808    0.000 1263.462    0.000 categorical.py:88(logits)
             2130437095 1219.413    0.000 1219.413    0.000 {built-in method torch._C._get_tracing_state}
              113939613 1209.186    0.000 1209.186    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               56686375  255.304    0.000 1199.310    0.000 utils.py:11(broadcast_all)
              170625988 1198.397    0.000 1198.397    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               56686375   69.934    0.000 1195.655    0.000 utils.py:82(probs_to_logits)
              170059125 1168.241    0.000 1168.241    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9278555956 1130.988    0.000 1147.538    0.000 {built-in method builtins.len}
              170059125  964.890    0.000  964.890    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8598274985  933.111    0.000  933.111    0.000 {method 'values' of 'collections.OrderedDict' objects}
               56686375  888.369    0.000  888.369    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              113372750  791.331    0.000  791.331    0.000 {built-in method broadcast_tensors}
                2267455  107.222    0.000  760.030    0.000 optimizer.py:189(zero_grad)
                2267455   84.015    0.000  753.825    0.000 replaybuffer.py:34(save_option_critic)
               56686375  152.769    0.000  708.492    0.000 utils.py:77(clamp_probs)
               56686375  122.800    0.000  666.709    0.000 layers.py:729(isFree)
               22674560  403.438    0.000  645.184    0.000 layer.py:151(update)
               13655202  297.840    0.000  636.786    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              171759714  627.136    0.000  627.136    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56686375  586.112    0.000  586.112    0.000 {built-in method bernoulli}
               56686375  567.535    0.000  567.535    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               56686375  555.723    0.000  555.723    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               57416376  547.354    0.000  547.354    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              388663187  441.902    0.000  543.910    0.000 layer.py:95(isFree)
               31744364  529.358    0.000  529.358    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15305323  515.090    0.000  515.090    0.000 {built-in method tensor}
              341251976  506.975    0.000  506.975    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               31744364  497.131    0.000  497.131    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              113372750  488.268    0.000  488.268    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56686375  474.058    0.000  474.058    0.000 {built-in method clamp}
               56686375  417.228    0.000  417.228    0.000 {built-in method log}
                6802369   17.163    0.000  415.091    0.000 game.py:37(board)
               56686375  401.112    0.000  401.112    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               31744350  388.239    0.000  388.239    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              751532905  248.539    0.000  387.887    0.000 {built-in method builtins.isinstance}
             1140940578  261.344    0.000  377.474    0.000 enum.py:646(__hash__)
               56686375  375.779    0.000  375.779    0.000 {built-in method all}
              176294639  354.327    0.000  354.327    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               56686375  352.492    0.000  352.492    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601855: <Lights2_option_critic_1> in cluster <dcc> Done

Job <Lights2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:04 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:06 2021
Terminated at Sun May  2 21:36:12 2021
Results reported at Sun May  2 21:36:12 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258190.67 sec.
    Max Memory :                                 1053 MB
    Average Memory :                             1042.15 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15331.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258914 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

