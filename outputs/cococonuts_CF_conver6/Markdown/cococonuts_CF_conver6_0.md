
# Parameters

    Name :                      cococonuts_CF_conver6-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Hours :                     24.0
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      62532849087 function calls (62221775116 primitive calls) in 86109.95 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.953 86109.953 {built-in method builtins.exec}
                      1    5.520    5.520 86109.953 86109.953 <string>:1(<module>)
                      1  332.116  332.116 86104.433 86104.433 main.py:94(CFagent)
               10707399   56.020    0.000 28189.900    0.003 agent.py:29(learn)
               10707389  741.232    0.000 22625.248    0.002 learner.py:42(Qlearn)
                3569133   24.446    0.000 21813.224    0.006 game.py:41(step)
                3569133   25.341    0.000 21004.278    0.006 layers.py:710(step)
                3569133  383.003    0.000 14087.043    0.004 layers.py:17(step)
              356468164 1414.763    0.000 13672.077    0.000 layer.py:98(move)
        348892070/37819790 1570.063    0.000 12297.131    0.000 module.py:866(_call_impl)
               27112401   80.519    0.000 11383.639    0.000 network.py:24(forward)
               27112401  372.039    0.000 11101.063    0.000 container.py:117(forward)
                3569133  462.208    0.000 11020.827    0.003 agent.py:54(_learn)
                3569133  454.363    0.000 9961.839    0.003 agent.py:208(_learn)
               10707389  116.109    0.000 8584.604    0.001 optimizer.py:84(wrapper)
               10707389   61.864    0.000 8118.084    0.001 grad_mode.py:24(decorate_context)
              356468164  956.331    0.000 8065.023    0.000 layers.py:727(check)
               10707389  378.650    0.000 7923.217    0.001 adam.py:55(step)
               10707389 1652.854    0.000 7144.745    0.001 _functional.py:53(adam)
                3569133 5671.569    0.002 7128.392    0.002 replaybuffer.py:22(sample_data)
                3569133  127.185    0.000 7121.057    0.002 agent.py:117(_learn)
                3569133  472.081    0.000 6922.041    0.002 agent.py:216(counterfact)
                3569134  554.687    0.000 6849.590    0.002 layers.py:676(update)
                3569133 4975.236    0.001 6222.413    0.002 replaybuffer.py:49(sample_data)
               10707389   52.059    0.000 6035.915    0.001 tensor.py:195(backward)
               10707389   61.327    0.000 5982.140    0.001 __init__.py:68(backward)
                8195384  283.379    0.000 5840.557    0.001 agent.py:49(__call__)
               10707389 5676.415    0.001 5676.415    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3569133 3004.590    0.001 5087.843    0.001 replaybuffer.py:28(teleporter_save_data)
                3569133 2181.177    0.001 4636.989    0.001 agent.py:88(interveen)
               49967869 2468.561    0.000 4169.822    0.000 layer.py:151(update)
               54224802  131.804    0.000 4135.635    0.000 conv.py:398(forward)
               54224802   90.806    0.000 3934.235    0.000 conv.py:390(_conv_forward)
               54224802 3843.429    0.000 3843.429    0.000 {built-in method conv2d}
               42894652 3526.969    0.000 3526.969    0.000 {built-in method tensor}
               34702111   27.909    0.000 3308.804    0.000 game.py:37(board)
              356231535  501.679    0.000 3256.044    0.000 layers.py:721(isFree)
              356468164 2375.768    0.000 3202.337    0.000 layers.py:464(check)
               74198937  162.422    0.000 3100.902    0.000 linear.py:93(forward)
               74198937   68.076    0.000 2849.533    0.000 functional.py:1737(linear)
                3569133 1822.872    0.001 2791.025    0.001 agent.py:67(modify)
               74198937 2766.356    0.000 2766.356    0.000 {built-in method torch._C._nn.linear}
             2255863072 2416.396    0.000 2754.366    0.000 layer.py:95(isFree)
              356468164 1680.463    0.000 2271.151    0.000 layers.py:71(check)
               51024930 2185.879    0.000 2185.879    0.000 {built-in method cat}
              186688271 1880.734    0.000 1880.734    0.000 {built-in method clone}
                3569123   82.092    0.000 1757.730    0.000 agent.py:167(__call__)
             6481891956 1155.956    0.000 1689.473    0.000 enum.py:646(__hash__)
               11764517   90.016    0.000 1668.645    0.000 agent.py:59(modify_board)
              101311338  100.441    0.000 1648.558    0.000 activation.py:713(forward)
                3569133   79.005    0.000 1607.258    0.000 agent.py:112(__call__)
                1071372   25.393    0.000 1550.579    0.001 agent.py:171(choose_action)
              101311338   93.711    0.000 1548.117    0.000 functional.py:1364(leaky_relu)
                1508543   22.417    0.000 1464.455    0.001 layers.py:731(restart)
              101311338 1436.755    0.000 1436.755    0.000 {built-in method torch._C._nn.leaky_relu}
              199871248 1388.871    0.000 1388.871    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1508543    9.995    0.000 1276.445    0.001 level.py:8(__init__)
              358973991  300.089    0.000 1268.957    0.000 {built-in method builtins.any}
               10707389  227.929    0.000 1241.110    0.000 optimizer.py:189(zero_grad)
              199871248 1226.442    0.000 1226.442    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1508543   75.291    0.000 1178.896    0.001 levels.py:262(generate)
                3569133   98.657    0.000 1150.752    0.000 replaybuffer.py:18(stacker)
              356913400  127.428    0.000 1146.373    0.000 {built-in method builtins.all}
               11764517 1099.971    0.000 1099.971    0.000 {built-in method torch._C._nn.one_hot}
             1341050339  362.045    0.000 1064.537    0.000 layers.py:682(<genexpr>)
              985747186 1043.795    0.000 1043.795    0.000 layer.py:146(elements)
               18671586  171.837    0.000 1032.165    0.000 level.py:41(notUsed)
              356468164  798.451    0.000 1008.794    0.000 layers.py:56(check)
             2843238856  796.301    0.000  968.868    0.000 layers.py:692(<genexpr>)
                3569123   91.471    0.000  956.397    0.000 replaybuffer.py:45(stacker)
               99935624  816.375    0.000  816.375    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               99935624  735.451    0.000  735.451    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7654153735  706.208    0.000  706.208    0.000 layer.py:91(positions)
               99935624  653.093    0.000  653.093    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               99935624  644.973    0.000  644.973    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8195384  217.806    0.000  614.857    0.000 exploration.py:53(softmaxer)
              699549452  491.610    0.000  605.523    0.000 tensor.py:906(grad)
                7138266  230.578    0.000  584.112    0.000 random.py:315(sample)
                3569133  330.139    0.000  561.081    0.000 collector.py:53(collect)
               10707389   21.994    0.000  554.820    0.000 loss.py:527(forward)
             6481932531  533.524    0.000  533.524    0.000 {built-in method builtins.hash}
               10707389   63.787    0.000  532.826    0.000 functional.py:2898(mse_loss)
              356468164  358.404    0.000  530.325    0.000 layers.py:42(check)
        6555443125/6555443122  452.320    0.000  522.714    0.000 {built-in method builtins.len}
              259087660  351.531    0.000  508.680    0.000 layers.py:107(isDone)
                3569133  159.074    0.000  493.518    0.000 replaybuffer.py:55(CF_save_data)
               99935624  482.029    0.000  482.029    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10707400  475.570    0.000  475.570    0.000 {built-in method nonzero}
               18671586   17.243    0.000  460.365    0.000 level.py:38(elementsIn)
              202021911  418.369    0.000  418.369    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              356199428  242.062    0.000  359.027    0.000 layer.py:126(remove)
               10707389  310.509    0.000  310.509    0.000 {built-in method torch._C._nn.mse_loss}
                1071372  249.115    0.000  296.532    0.000 agent.py:182(convert_values)
               18671586  144.205    0.000  291.050    0.000 level.py:39(<listcomp>)
              443153161  213.997    0.000  284.070    0.000 layer.py:130(add)
               10708564  279.066    0.000  279.066    0.000 {built-in method max}
               54224802   41.252    0.000  263.377    0.000 flatten.py:39(forward)
              832980363  263.048    0.000  263.048    0.000 level.py:32(inverse)
              379036738  167.972    0.000  253.011    0.000 random.py:250(_randbelow_with_getrandbits)
               21414798  243.805    0.000  243.805    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9501862: <cococonuts_CF_conver6_0> in cluster <dcc> Done

Job <cococonuts_CF_conver6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:07 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 16:54:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 16:54:31 2021
Terminated at Thu Apr  8 16:49:45 2021
Results reported at Thu Apr  8 16:49:45 2021

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

    CPU time :                                   85904.44 sec.
    Max Memory :                                 10105 MB
    Average Memory :                             6651.01 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            90218 sec.

The output (if any) is above this job summary.

