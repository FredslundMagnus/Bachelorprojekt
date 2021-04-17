
# Parameters

    Name :                      TEST_CF_CAUSAL4_6c1-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     23.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                6
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      72725444990 function calls (72381148083 primitive calls) in 82515.61 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82515.611 82515.611 {built-in method builtins.exec}
                      1    5.653    5.653 82515.611 82515.611 <string>:1(<module>)
                      1  266.338  266.338 82509.958 82509.958 main.py:95(CFagent)
               11278377   40.428    0.000 26150.466    0.002 agent.py:29(learn)
               11278362  667.971    0.000 21176.404    0.002 learner.py:42(Qlearn)
                3759459   18.096    0.000 20783.844    0.006 game.py:41(step)
                3759459   23.679    0.000 19936.912    0.005 layers.py:710(step)
                3759459  323.765    0.000 12979.601    0.003 layers.py:17(step)
              375437228 1007.924    0.000 12625.774    0.000 layer.py:98(move)
        385517999/41222783 1481.714    0.000 11997.594    0.000 module.py:866(_call_impl)
               29944421   76.744    0.000 11209.675    0.000 network.py:24(forward)
               29944421  357.194    0.000 10950.017    0.000 container.py:117(forward)
                3759459  847.104    0.000 10817.725    0.003 agent.py:217(counterfact)
                3759459  406.232    0.000 10175.943    0.003 agent.py:54(_learn)
                3759459  400.911    0.000 9347.614    0.002 agent.py:209(_learn)
               11278362   96.152    0.000 8262.502    0.001 optimizer.py:84(wrapper)
               11278362   46.192    0.000 7850.930    0.001 grad_mode.py:24(decorate_context)
               11278362  325.090    0.000 7700.131    0.001 adam.py:55(step)
              375437228 1101.052    0.000 7207.329    0.000 layers.py:727(check)
               11278362 1607.279    0.000 7005.105    0.001 _functional.py:53(adam)
                3759460  547.043    0.000 6898.566    0.002 layers.py:676(update)
                3759459  111.301    0.000 6563.558    0.002 agent.py:117(_learn)
               59006772 5920.714    0.000 5920.714    0.000 {built-in method tensor}
                3759459 4488.554    0.001 5759.231    0.002 replaybuffer.py:22(sample_data)
               50396042   31.194    0.000 5724.701    0.000 game.py:37(board)
                9325229  240.876    0.000 5716.404    0.001 agent.py:49(__call__)
               11278362   42.509    0.000 5448.977    0.000 tensor.py:195(backward)
               11278362   42.347    0.000 5404.971    0.000 __init__.py:68(backward)
               11278362 5152.294    0.000 5152.294    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3759459 3882.943    0.001 4986.355    0.001 replaybuffer.py:49(sample_data)
               75189190 2821.445    0.000 4818.956    0.000 layer.py:151(update)
               59888842  134.317    0.000 4094.989    0.000 conv.py:398(forward)
                3759459 2259.865    0.001 3969.689    0.001 replaybuffer.py:28(teleporter_save_data)
                3759459 1686.349    0.000 3956.984    0.001 agent.py:88(interveen)
               59888842   83.314    0.000 3898.353    0.000 conv.py:390(_conv_forward)
               59888842 3815.038    0.000 3815.038    0.000 {built-in method conv2d}
              375198853  674.499    0.000 3735.335    0.000 layers.py:721(isFree)
               82314345  155.775    0.000 3069.791    0.000 linear.py:93(forward)
             3487858590 2541.409    0.000 3060.836    0.000 layer.py:95(isFree)
               82314345   66.157    0.000 2833.180    0.000 functional.py:1737(linear)
               82314345 2750.958    0.000 2750.958    0.000 {built-in method torch._C._nn.linear}
                3759459 1731.462    0.000 2622.955    0.001 agent.py:67(modify)
                1821927   37.458    0.000 2389.524    0.001 agent.py:172(choose_action)
               54438662 1979.031    0.000 1979.031    0.000 {built-in method cat}
             7325836118 1180.664    0.000 1702.730    0.000 enum.py:646(__hash__)
              176447311 1659.475    0.000 1659.475    0.000 {built-in method clone}
              376244849  363.359    0.000 1627.663    0.000 {built-in method builtins.any}
              112258766   90.906    0.000 1624.622    0.000 activation.py:713(forward)
                3759444   66.755    0.000 1618.451    0.000 agent.py:168(__call__)
               13084688   77.102    0.000 1612.335    0.000 agent.py:59(modify_board)
              112258766   90.233    0.000 1533.716    0.000 functional.py:1364(leaky_relu)
                3759459   62.461    0.000 1525.297    0.000 agent.py:112(__call__)
              112258766 1426.611    0.000 1426.611    0.000 {built-in method torch._C._nn.leaky_relu}
              210529404 1383.885    0.000 1383.885    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              375437228 1025.507    0.000 1352.642    0.000 layers.py:71(check)
             4097339279 1048.004    0.000 1264.304    0.000 layers.py:692(<genexpr>)
              210529404 1221.963    0.000 1221.963    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11278362  220.491    0.000 1214.425    0.000 optimizer.py:189(zero_grad)
                3460611   45.749    0.000 1210.346    0.000 layers.py:731(restart)
              375437228  743.618    0.000 1148.239    0.000 layers.py:240(check)
             1211156697 1146.462    0.000 1146.462    0.000 layer.py:146(elements)
               13084688 1065.645    0.000 1065.645    0.000 {built-in method torch._C._nn.one_hot}
              375437228  654.830    0.000 1064.264    0.000 layers.py:280(check)
                3759459   77.550    0.000 1008.652    0.000 replaybuffer.py:18(stacker)
                3460611   19.809    0.000  850.100    0.000 level.py:8(__init__)
                3759444   74.541    0.000  848.927    0.000 replaybuffer.py:45(stacker)
              375946000   70.488    0.000  835.721    0.000 {built-in method builtins.all}
              786852319  171.072    0.000  810.749    0.000 layers.py:682(<genexpr>)
              105264702  798.498    0.000  798.498    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9026783346  782.437    0.000  782.437    0.000 layer.py:91(positions)
              375437228  594.266    0.000  755.311    0.000 layers.py:56(check)
                3759459  289.972    0.000  706.618    0.000 replaybuffer.py:55(CF_save_data)
              105264702  698.759    0.000  698.759    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3460611  112.357    0.000  683.337    0.000 levels.py:199(generate)
              105264702  636.743    0.000  636.743    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              375946000  433.562    0.000  633.655    0.000 layers.py:107(isDone)
              105264702  632.712    0.000  632.712    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        9252519219/9252519216  552.852    0.000  624.055    0.000 {built-in method builtins.len}
              375437228  401.762    0.000  610.789    0.000 layers.py:267(check)
              375437228  385.202    0.000  581.342    0.000 layers.py:307(check)
              736852998  463.471    0.000  574.692    0.000 tensor.py:906(grad)
                9325229  210.419    0.000  564.455    0.000 exploration.py:53(softmaxer)
               14440140  210.386    0.000  556.564    0.000 random.py:315(sample)
                3759459  318.280    0.000  541.784    0.000 collector.py:53(collect)
             7325878821  522.073    0.000  522.073    0.000 {built-in method builtins.hash}
              375437228  342.767    0.000  499.091    0.000 layers.py:42(check)
                1821927  412.154    0.000  483.484    0.000 agent.py:183(convert_values)
              105264702  472.792    0.000  472.792    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11278362   16.449    0.000  464.727    0.000 loss.py:527(forward)
                6921222   55.880    0.000  463.971    0.000 level.py:41(notUsed)
               11278362   43.185    0.000  448.277    0.000 functional.py:2898(mse_loss)
               11278378  426.825    0.000  426.825    0.000 {built-in method nonzero}
              193291443  373.541    0.000  373.541    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               34606110   46.747    0.000  303.905    0.000 layer.py:69(restart)
              325984145  205.032    0.000  292.815    0.000 layer.py:126(remove)
               75189190  285.762    0.000  285.762    0.000 layer.py:163(<listcomp>)
              531055178  206.667    0.000  285.551    0.000 layer.py:130(add)
             2743364684  275.369    0.000  275.369    0.000 layer.py:203(isBlocking)
              448546793  184.954    0.000  274.681    0.000 random.py:250(_randbelow_with_getrandbits)
               11278362  272.834    0.000  272.834    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9505791: <TEST_CF_CAUSAL4_6c1_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_6c1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 01:04:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 01:04:21 2021
Terminated at Fri Apr  9 23:59:45 2021
Results reported at Fri Apr  9 23:59:45 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   82316.45 sec.
    Max Memory :                                 10472 MB
    Average Memory :                             6880.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5912.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82525 sec.
    Turnaround time :                            83705 sec.

The output (if any) is above this job summary.

