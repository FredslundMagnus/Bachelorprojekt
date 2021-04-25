
# Parameters

    Name :                      MagicalLights2_convert4-1
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      53227329996 function calls (52954526101 primitive calls) in 86113.67 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.669 86113.669 {built-in method builtins.exec}
                      1    4.179    4.179 86113.669 86113.669 <string>:1(<module>)
                      1  290.932  290.932 86109.490 86109.490 main.py:79(CFagent)
                7874451   30.355    0.000 23526.671    0.003 agent.py:29(learn)
                7874451  593.748    0.000 19606.773    0.002 learner.py:42(Qlearn)
                2624817 5211.025    0.002 18861.793    0.007 agent.py:210(counterfact)
                2624817   11.864    0.000 14095.027    0.005 game.py:41(step)
                2624817   16.010    0.000 13447.290    0.005 layers.py:718(step)
                2624818  405.172    0.000 13268.375    0.005 layers.py:684(update)
        304285111/31482907 1226.943    0.000 11142.312    0.000 module.py:866(_call_impl)
               23608456   65.133    0.000 10487.369    0.000 network.py:27(forward)
               23608456  323.364    0.000 10279.506    0.000 container.py:117(forward)
                2624817  268.576    0.000 9071.769    0.003 agent.py:54(_learn)
                2624817  269.867    0.000 8426.108    0.003 agent.py:202(_learn)
                7874451   68.848    0.000 8303.632    0.001 optimizer.py:84(wrapper)
                7874451   32.916    0.000 7986.701    0.001 grad_mode.py:24(decorate_context)
                7874451  230.985    0.000 7881.132    0.001 adam.py:55(step)
               23959777  205.592    0.000 7619.949    0.000 layers.py:740(restart)
                7874451 1616.962    0.000 7395.409    0.001 _functional.py:53(adam)
               64183722 7037.792    0.000 7037.792    0.000 {built-in method tensor}
               58074950   36.678    0.000 6875.219    0.000 game.py:37(board)
                2624817 4187.457    0.002 6085.590    0.002 replaybuffer.py:73(CF_save_data)
                2624817   79.750    0.000 5982.322    0.002 agent.py:117(_learn)
                7866992  216.525    0.000 5662.223    0.001 agent.py:49(__call__)
                2624817 3003.185    0.001 5564.855    0.002 replaybuffer.py:28(teleporter_save_data)
               23959777   95.942    0.000 5338.440    0.000 level.py:8(__init__)
               52496350 3476.320    0.000 5016.387    0.000 layer.py:151(update)
                7874451   32.448    0.000 4853.848    0.001 tensor.py:195(backward)
                7874451   30.031    0.000 4820.178    0.001 __init__.py:68(backward)
                2624817 2783.894    0.001 4680.404    0.002 agent.py:88(interveen)
                7874451 4614.780    0.001 4614.780    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               23959777  728.663    0.000 4496.606    0.000 levels.py:199(generate)
                2624817 3457.111    0.001 4291.565    0.002 replaybuffer.py:22(sample_data)
                2624817 3446.832    0.001 4262.967    0.002 replaybuffer.py:67(sample_data)
                2617379   61.028    0.000 4033.682    0.002 agent.py:175(choose_action)
               47216912   99.852    0.000 3673.938    0.000 conv.py:398(forward)
              288856664 3632.012    0.000 3632.012    0.000 {built-in method clone}
               47216912   59.587    0.000 3528.045    0.000 conv.py:390(_conv_forward)
               47216912 3468.458    0.000 3468.458    0.000 {built-in method conv2d}
               47919554  326.124    0.000 3078.036    0.000 level.py:41(notUsed)
               65575734  127.700    0.000 3008.479    0.000 linear.py:93(forward)
               65575734   55.158    0.000 2819.113    0.000 functional.py:1737(linear)
               65575734 2750.866    0.000 2750.866    0.000 {built-in method torch._C._nn.linear}
                2624817 1417.804    0.001 2182.867    0.001 agent.py:67(modify)
              239597770  269.371    0.000 2002.818    0.000 layer.py:69(restart)
               89184190   74.536    0.000 1680.161    0.000 activation.py:713(forward)
               89184190   77.312    0.000 1605.625    0.000 functional.py:1364(leaky_relu)
               10491809   73.590    0.000 1525.995    0.000 agent.py:59(modify_board)
              146989752 1525.380    0.000 1525.380    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               89184190 1512.872    0.000 1512.872    0.000 {built-in method torch._C._nn.leaky_relu}
               36739979 1485.742    0.000 1485.742    0.000 {built-in method cat}
              146989752 1331.955    0.000 1331.955    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2624817   46.304    0.000 1323.567    0.001 agent.py:171(__call__)
              973964087 1245.714    0.000 1245.714    0.000 level.py:32(inverse)
                2624817   44.675    0.000 1239.813    0.000 agent.py:112(__call__)
               47919554   39.876    0.000 1180.514    0.000 level.py:38(elementsIn)
              262481800  180.835    0.000 1178.115    0.000 {built-in method builtins.all}
                7874451  185.971    0.000 1157.601    0.000 optimizer.py:189(zero_grad)
               23959877  563.702    0.000 1139.934    0.000 layers.py:36(reset)
              241146841  245.123    0.000 1073.950    0.000 {built-in method builtins.any}
             2093537868  559.608    0.000 1030.509    0.000 layers.py:690(<genexpr>)
             4400312423  692.906    0.000 1009.357    0.000 enum.py:646(__hash__)
               10491809  974.459    0.000  974.459    0.000 {built-in method torch._C._nn.one_hot}
             3154080260  953.163    0.000  953.163    0.000 layer.py:146(elements)
              301973290  889.464    0.000  889.464    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               73494876  831.951    0.000  831.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2623742253  687.850    0.000  828.827    0.000 layers.py:700(<genexpr>)
                2617379  673.189    0.000  804.899    0.000 agent.py:186(convert_values)
               47919554  350.939    0.000  712.778    0.000 level.py:39(<listcomp>)
               73494876  709.199    0.000  709.199    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1524549895  509.509    0.000  694.033    0.000 layer.py:130(add)
               73494876  682.146    0.000  682.146    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               73494876  675.961    0.000  675.961    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               23959777  316.740    0.000  673.692    0.000 level.py:16(<dictcomp>)
               53169188  256.051    0.000  665.758    0.000 random.py:315(sample)
                2624817   45.391    0.000  648.760    0.000 replaybuffer.py:18(stacker)
                2624817   45.624    0.000  637.472    0.000 replaybuffer.py:63(stacker)
                7866992  218.136    0.000  590.966    0.000 exploration.py:53(softmaxer)
               25219667  568.944    0.000  586.332    0.000 layer.py:126(remove)
               48014688  566.614    0.000  566.614    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2624817  325.212    0.000  538.894    0.000 collector.py:46(collect)
               73494876  530.086    0.000  530.086    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        6547547123/6547547120  415.500    0.000  469.428    0.000 {built-in method builtins.len}
             2587657514  450.490    0.000  450.490    0.000 enum.py:352(<genexpr>)
               47919554  250.595    0.000  427.859    0.000 {built-in method _functools.reduce}
              514464216  342.570    0.000  423.517    0.000 tensor.py:906(grad)
                7874451   13.032    0.000  383.443    0.000 loss.py:527(forward)
                7874451   30.253    0.000  370.411    0.000 functional.py:2898(mse_loss)
             4400342470  316.456    0.000  316.456    0.000 {built-in method builtins.hash}
              433092703  200.637    0.000  289.016    0.000 random.py:250(_randbelow_with_getrandbits)
             4302163653  284.830    0.000  284.830    0.000 {method 'append' of 'list' objects}
              262481800  173.603    0.000  281.386    0.000 layers.py:113(isDone)
               47216912   33.834    0.000  275.732    0.000 flatten.py:39(forward)
                7874451  243.550    0.000  243.550    0.000 {built-in method torch._C._nn.mse_loss}
               47216912  241.898    0.000  241.898    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1964710734  235.920    0.000  235.920    0.000 layer.py:182(grid)
               15748902  229.023    0.000  229.023    0.000 {built-in method sum}
                5249636  224.526    0.000  224.526    0.000 {built-in method nonzero}
                7875499  218.490    0.000  218.490    0.000 {built-in method max}
              312153696  214.582    0.000  214.582    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571372: <MagicalLights2_convert4_1> in cluster <dcc> Done

Job <MagicalLights2_convert4_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:48:00 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:48:00 2021
Terminated at Sun Apr 25 18:43:21 2021
Results reported at Sun Apr 25 18:43:21 2021

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

    CPU time :                                   85894.72 sec.
    Max Memory :                                 8496 MB
    Average Memory :                             5913.96 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7888.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            86815 sec.

The output (if any) is above this job summary.

