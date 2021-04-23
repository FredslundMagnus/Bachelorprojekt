
# Parameters

    Name :                      Causal4_Cf_convert2_TopN3-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64430587521 function calls (64149245538 primitive calls) in 86110.43 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.434 86110.434 {built-in method builtins.exec}
                      1    4.840    4.840 86110.434 86110.434 <string>:1(<module>)
                      1  415.072  415.072 86105.594 86105.594 main.py:79(CFagent)
                9001851   49.555    0.000 24968.579    0.003 agent.py:29(learn)
                3000617   18.964    0.000 20645.322    0.007 game.py:41(step)
                9001849  662.837    0.000 20011.552    0.002 learner.py:42(Qlearn)
                3000617   21.463    0.000 19828.726    0.007 layers.py:718(step)
                3000617  303.692    0.000 12794.552    0.004 layers.py:17(step)
              300061700  910.575    0.000 12464.427    0.000 layer.py:98(move)
        314787371/33447079 1418.063    0.000 11502.959    0.000 module.py:866(_call_impl)
               24445230   77.182    0.000 10662.651    0.000 network.py:27(forward)
               24445230  358.567    0.000 10396.908    0.000 container.py:117(forward)
                3000617  910.562    0.000 10283.790    0.003 agent.py:210(counterfact)
                3000617  391.558    0.000 9727.945    0.003 agent.py:54(_learn)
                3000617  386.086    0.000 8772.079    0.003 agent.py:202(_learn)
                3000617 6784.610    0.002 7853.838    0.003 replaybuffer.py:22(sample_data)
              300061700 1426.554    0.000 7597.763    0.000 layers.py:735(check)
                9001849  110.239    0.000 7543.071    0.001 optimizer.py:84(wrapper)
                3000617 6279.333    0.002 7298.984    0.002 replaybuffer.py:67(sample_data)
                9001849   59.022    0.000 7070.455    0.001 grad_mode.py:24(decorate_context)
                3000618  485.215    0.000 6977.528    0.002 layers.py:684(update)
                9001849  327.224    0.000 6888.835    0.001 adam.py:55(step)
                3000617  108.246    0.000 6393.912    0.002 agent.py:117(_learn)
                9001849 1435.629    0.000 6231.629    0.001 _functional.py:53(adam)
                7719856  280.894    0.000 5835.841    0.001 agent.py:49(__call__)
                9001849   46.051    0.000 5443.970    0.001 tensor.py:195(backward)
                9001849   51.589    0.000 5396.429    0.001 __init__.py:68(backward)
               47857605 5237.600    0.000 5237.600    0.000 {built-in method tensor}
                9001849 5118.147    0.001 5118.147    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               40918775   29.937    0.000 5047.968    0.000 game.py:37(board)
               60012350 2853.123    0.000 4863.558    0.000 layer.py:151(update)
                3000617 2111.935    0.001 4311.337    0.001 agent.py:88(interveen)
                3000617 2374.482    0.001 4110.079    0.001 replaybuffer.py:28(teleporter_save_data)
               48890460  118.233    0.000 3974.602    0.000 conv.py:398(forward)
               48890460   85.382    0.000 3795.818    0.000 conv.py:390(_conv_forward)
               48890460 3710.436    0.000 3710.436    0.000 {built-in method conv2d}
              300061700  557.719    0.000 3317.862    0.000 layers.py:729(isFree)
               67334456  147.897    0.000 2911.519    0.000 linear.py:93(forward)
             2623782186 2310.947    0.000 2760.143    0.000 layer.py:95(isFree)
               67334456   60.568    0.000 2685.033    0.000 functional.py:1737(linear)
               67334456 2610.808    0.000 2610.808    0.000 {built-in method torch._C._nn.linear}
                3000617 1663.494    0.001 2582.041    0.001 agent.py:67(modify)
                1722293   44.136    0.000 2562.914    0.001 agent.py:175(choose_action)
               40726633 1692.590    0.000 1692.590    0.000 {built-in method cat}
              160349489 1683.726    0.000 1683.726    0.000 {built-in method clone}
               10720473   90.171    0.000 1681.323    0.000 agent.py:59(modify_board)
             5928482029 1111.414    0.000 1580.298    0.000 enum.py:646(__hash__)
                3000615   68.222    0.000 1571.675    0.001 agent.py:171(__call__)
               91779686   91.631    0.000 1483.995    0.000 activation.py:713(forward)
              299873338  318.676    0.000 1413.194    0.000 {built-in method builtins.any}
               91779686   81.591    0.000 1392.364    0.000 functional.py:1364(leaky_relu)
                3000617   66.145    0.000 1380.443    0.000 agent.py:112(__call__)
               91779686 1295.382    0.000 1295.382    0.000 {built-in method torch._C._nn.leaky_relu}
                3189080   43.504    0.000 1247.382    0.000 layers.py:740(restart)
             1054796606 1245.258    0.000 1245.258    0.000 layer.py:146(elements)
                3000617  963.437    0.000 1220.567    0.000 replaybuffer.py:73(CF_save_data)
              300061700  927.396    0.000 1209.230    0.000 layers.py:77(check)
              168034512 1199.711    0.000 1199.711    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              300061700  770.100    0.000 1166.247    0.000 layers.py:246(check)
              300061800  138.194    0.000 1133.010    0.000 {built-in method builtins.all}
               10720473 1115.533    0.000 1115.533    0.000 {built-in method torch._C._nn.one_hot}
             3265599920  903.899    0.000 1094.519    0.000 layers.py:700(<genexpr>)
                9001849  199.077    0.000 1081.708    0.000 optimizer.py:189(zero_grad)
              168034512 1064.910    0.000 1064.910    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1510660888  396.371    0.000 1033.443    0.000 layers.py:690(<genexpr>)
              300061700  609.265    0.000 1004.397    0.000 layers.py:286(check)
                3189080   21.951    0.000  880.186    0.000 level.py:8(__init__)
                3000617   71.210    0.000  803.260    0.000 replaybuffer.py:18(stacker)
                3000615   72.991    0.000  763.551    0.000 replaybuffer.py:63(stacker)
             7777683767  706.748    0.000  706.748    0.000 layer.py:91(positions)
               84017256  703.181    0.000  703.181    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              300061700  553.420    0.000  703.056    0.000 layers.py:62(check)
                3189080  113.116    0.000  692.812    0.000 levels.py:199(generate)
                7719856  214.546    0.000  627.405    0.000 exploration.py:53(softmaxer)
               84017256  626.745    0.000  626.745    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        7931849698/7931849695  535.308    0.000  600.226    0.000 {built-in method builtins.len}
               84017256  590.762    0.000  590.762    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84017256  586.117    0.000  586.117    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              300061800  392.748    0.000  572.922    0.000 layers.py:113(isDone)
               12379394  221.304    0.000  567.233    0.000 random.py:315(sample)
                9001849   24.634    0.000  514.361    0.000 loss.py:527(forward)
              300061700  318.735    0.000  507.525    0.000 layers.py:273(check)
              300061700  324.328    0.000  505.102    0.000 layers.py:313(check)
              588120876  402.691    0.000  500.022    0.000 tensor.py:906(grad)
                9001849   53.384    0.000  489.726    0.000 functional.py:2898(mse_loss)
                3000617  279.847    0.000  480.620    0.000 collector.py:46(collect)
                1722293  424.563    0.000  480.402    0.000 agent.py:186(convert_values)
             5928516332  468.891    0.000  468.891    0.000 {built-in method builtins.hash}
                6378160   55.471    0.000  467.233    0.000 level.py:41(notUsed)
              300061700  299.842    0.000  436.885    0.000 layers.py:48(check)
               84017256  426.620    0.000  426.620    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              174070577  363.644    0.000  363.644    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              300061700  232.985    0.000  336.678    0.000 layers.py:23(check)
               31890800   46.320    0.000  313.122    0.000 layer.py:69(restart)
              284457019  212.278    0.000  305.397    0.000 layer.py:126(remove)
              468467192  213.478    0.000  299.777    0.000 layer.py:130(add)
                9001849  291.607    0.000  291.607    0.000 {built-in method torch._C._nn.mse_loss}
             3313246557  280.748    0.000  280.748    0.000 {method 'random' of '_random.Random' objects}
                6001236  279.536    0.000  279.536    0.000 {built-in method nonzero}
              376133403  182.872    0.000  272.780    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551814: <Causal4_Cf_convert2_TopN3_2> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 03:23:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 03:23:18 2021
Terminated at Fri Apr 23 03:18:35 2021
Results reported at Fri Apr 23 03:18:35 2021

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

    CPU time :                                   85905.52 sec.
    Max Memory :                                 8904 MB
    Average Memory :                             6059.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7480.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            172684 sec.

The output (if any) is above this job summary.

