
# Parameters

    Name :                      Diamonds2_convert4-2
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67847491021 function calls (67549371838 primitive calls) in 86109.54 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.538 86109.538 {built-in method builtins.exec}
                      1    4.736    4.736 86109.538 86109.538 <string>:1(<module>)
                      1  392.999  392.999 86104.803 86104.803 main.py:80(CFagent)
                9166551   38.918    0.000 23146.854    0.003 agent.py:29(learn)
                9166546  586.355    0.000 18717.201    0.002 learner.py:42(Qlearn)
                3055517   15.248    0.000 18627.277    0.006 game.py:42(step)
                3055517   23.472    0.000 17914.074    0.006 layers.py:827(step)
        333145668/35028176 1442.998    0.000 11219.916    0.000 module.py:866(_call_impl)
               25861630   76.171    0.000 10508.059    0.000 network.py:28(forward)
                3055517 1117.908    0.000 10292.542    0.003 agent.py:212(counterfact)
               25861630  348.462    0.000 10240.741    0.000 container.py:117(forward)
                3055517  299.304    0.000 10221.788    0.003 layers.py:17(step)
              305028879  531.070    0.000 9892.829    0.000 layer.py:106(move)
                3055517  356.806    0.000 9016.969    0.003 agent.py:54(_learn)
                3055517  356.498    0.000 8229.016    0.003 agent.py:204(_learn)
                3055518  468.453    0.000 7636.703    0.002 layers.py:793(update)
                3055517 6352.721    0.002 7385.158    0.002 replaybuffer.py:22(sample_data)
                9166546   80.145    0.000 7232.276    0.001 optimizer.py:84(wrapper)
                3055517 4238.459    0.001 7230.208    0.002 replaybuffer.py:28(teleporter_save_data)
                3055517 6199.170    0.002 7178.856    0.002 replaybuffer.py:67(sample_data)
                9166546   42.251    0.000 6871.722    0.001 grad_mode.py:24(decorate_context)
                9166546  308.238    0.000 6734.298    0.001 adam.py:55(step)
              305028879 1262.037    0.000 6272.010    0.000 layers.py:844(check)
                9166546 1400.323    0.000 6107.425    0.001 _functional.py:53(adam)
                3055517  101.083    0.000 5840.499    0.002 agent.py:117(_learn)
                3055517 3570.634    0.001 5591.405    0.002 agent.py:88(interveen)
                8346480  244.319    0.000 5590.812    0.001 agent.py:49(__call__)
                9166546   38.594    0.000 4905.108    0.001 tensor.py:195(backward)
                9166546   42.904    0.000 4865.074    0.001 __init__.py:68(backward)
               47966580 4710.521    0.000 4710.521    0.000 {built-in method tensor}
                9166546 4636.569    0.001 4636.569    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               40906970   27.916    0.000 4528.687    0.000 game.py:38(board)
               54999315 2137.679    0.000 3824.953    0.000 layer.py:175(NoRock_update)
               51723260  116.458    0.000 3789.302    0.000 conv.py:398(forward)
               51723260   76.349    0.000 3613.669    0.000 conv.py:390(_conv_forward)
               51723260 3537.320    0.000 3537.320    0.000 {built-in method conv2d}
                2237575   49.428    0.000 3212.514    0.001 agent.py:176(choose_action)
                5058711   59.326    0.000 2869.327    0.001 layers.py:849(restart)
               71473856  147.987    0.000 2866.030    0.000 linear.py:93(forward)
              281651629 2780.710    0.000 2780.710    0.000 {built-in method clone}
               71473856   62.010    0.000 2640.342    0.000 functional.py:1737(linear)
               71473856 2564.098    0.000 2564.098    0.000 {built-in method torch._C._nn.linear}
              305028879  571.174    0.000 2548.557    0.000 layers.py:838(isFree)
                5058711   28.452    0.000 2406.851    0.000 level.py:8(__init__)
                3055517 1591.907    0.001 2381.804    0.001 agent.py:67(modify)
                5058711   82.235    0.000 2119.921    0.000 levels.py:249(generate)
             2734713858 1655.640    0.000 1977.383    0.000 layer.py:103(isFree)
               32884410  338.055    0.000 1954.907    0.000 level.py:41(notUsed)
               41957142 1665.416    0.000 1665.416    0.000 {built-in method cat}
             6484199574 1142.162    0.000 1651.732    0.000 enum.py:646(__hash__)
                3055517 1188.319    0.000 1546.753    0.001 replaybuffer.py:73(CF_save_data)
               11401997   80.001    0.000 1541.844    0.000 agent.py:59(modify_board)
               97335486   80.798    0.000 1506.186    0.000 activation.py:713(forward)
                3055512   60.966    0.000 1427.785    0.000 agent.py:172(__call__)
               97335486   79.773    0.000 1425.388    0.000 functional.py:1364(leaky_relu)
                3055517   58.056    0.000 1350.583    0.000 agent.py:112(__call__)
               97335486 1328.832    0.000 1328.832    0.000 {built-in method torch._C._nn.leaky_relu}
              303548607  298.426    0.000 1279.018    0.000 {built-in method builtins.any}
              171108852 1198.928    0.000 1198.928    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                9166546  190.875    0.000 1062.416    0.000 optimizer.py:189(zero_grad)
              171108852 1055.038    0.000 1055.038    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11401997 1017.721    0.000 1017.721    0.000 {built-in method torch._C._nn.one_hot}
             1083519973  999.529    0.000  999.529    0.000 layer.py:154(elements)
             3004930890  802.956    0.000  980.592    0.000 layers.py:809(<genexpr>)
               32884410   26.445    0.000  946.201    0.000 level.py:38(elementsIn)
              305028879  600.735    0.000  940.429    0.000 layers.py:337(check)
              305551800  131.148    0.000  929.295    0.000 {built-in method builtins.all}
              305028879  582.613    0.000  914.238    0.000 layers.py:375(check)
              305028879  556.358    0.000  885.311    0.000 layers.py:349(check)
              305028879  550.170    0.000  870.547    0.000 layers.py:387(check)
             1383163089  383.499    0.000  836.031    0.000 layers.py:799(<genexpr>)
                3055517   65.157    0.000  780.449    0.000 replaybuffer.py:18(stacker)
                3055512   61.396    0.000  740.844    0.000 replaybuffer.py:63(stacker)
             7112380063  719.833    0.000  719.833    0.000 layer.py:99(positions)
               85554426  696.270    0.000  696.270    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2237575  581.823    0.000  674.546    0.000 agent.py:187(convert_values)
               32884410  304.809    0.000  613.159    0.000 level.py:39(<listcomp>)
               85554426  612.566    0.000  612.566    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              296109138  609.384    0.000  609.384    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        7578179212/7578179209  520.223    0.000  579.746    0.000 {built-in method builtins.len}
                8346480  212.934    0.000  571.776    0.000 exploration.py:53(softmaxer)
               85554426  561.790    0.000  561.790    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               85554426  560.536    0.000  560.536    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6484234437  509.576    0.000  509.576    0.000 {built-in method builtins.hash}
              598881066  400.380    0.000  495.703    0.000 tensor.py:906(grad)
                6111034  185.079    0.000  479.127    0.000 random.py:315(sample)
                3055517  278.664    0.000  473.856    0.000 collector.py:46(collect)
               85554426  419.949    0.000  419.949    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9166546   14.722    0.000  412.028    0.000 loss.py:527(forward)
              305028879  256.904    0.000  401.131    0.000 layers.py:326(check)
                9166546   41.672    0.000  397.306    0.000 functional.py:2898(mse_loss)
              305028879  248.958    0.000  388.757    0.000 layers.py:364(check)
               45528399   41.934    0.000  387.202    0.000 layer.py:77(restart)
             1550932207  386.013    0.000  386.013    0.000 level.py:32(inverse)
              305028879  227.706    0.000  336.355    0.000 layers.py:23(check)
             1631556368  310.735    0.000  310.735    0.000 enum.py:352(<genexpr>)
              489249188  215.161    0.000  309.537    0.000 layer.py:138(add)
               32884410  191.614    0.000  306.597    0.000 {built-in method _functools.reduce}
                5058811  136.641    0.000  270.936    0.000 layers.py:36(reset)
              135139383  178.778    0.000  270.459    0.000 layers.py:113(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678090: <Diamonds2_convert4_2> in cluster <dcc> Done

Job <Diamonds2_convert4_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:40 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May 23 20:25:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 23 20:25:05 2021
Terminated at Mon May 24 20:20:18 2021
Results reported at Mon May 24 20:20:18 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85895.94 sec.
    Max Memory :                                 8867 MB
    Average Memory :                             6033.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7517.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            261458 sec.

The output (if any) is above this job summary.

