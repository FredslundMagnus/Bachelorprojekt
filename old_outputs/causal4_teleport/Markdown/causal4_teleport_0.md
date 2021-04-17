
# Parameters

    Name :                      causal4_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal4
    Hours :                     16.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                0
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      51349653455 function calls (51142503612 primitive calls) in 57313.55 seconds

##    Ordered by: cumulative time
   List reduced from 490 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57313.552 57313.552 {built-in method builtins.exec}
                      1    1.880    1.880 57313.552 57313.552 <string>:1(<module>)
                      1  174.813  174.813 57311.672 57311.672 main.py:42(teleport)
                7411040   27.087    0.000 21108.581    0.003 agent.py:29(learn)
                7411040  545.746    0.000 17830.965    0.002 learner.py:42(Qlearn)
                3705520   15.515    0.000 16810.335    0.005 game.py:35(step)
                3705520   19.107    0.000 15905.627    0.004 layers.py:448(step)
                3705520  400.312    0.000 12736.738    0.003 agent.py:54(_learn)
                3705520  280.988    0.000 11311.106    0.003 layers.py:17(step)
              370552000  834.328    0.000 10999.252    0.000 layer.py:84(move)
        233057448/25908616  941.966    0.000 8532.541    0.000 module.py:866(_call_impl)
                3705520  107.247    0.000 8328.309    0.002 agent.py:115(_learn)
               18497576   54.298    0.000 7947.007    0.000 network.py:24(forward)
               18497576  252.304    0.000 7781.479    0.000 container.py:117(forward)
                7411040   64.657    0.000 7494.621    0.001 optimizer.py:84(wrapper)
                7411040   31.981    0.000 7188.826    0.001 grad_mode.py:24(decorate_context)
                7411040  204.295    0.000 7088.681    0.001 adam.py:55(step)
                7411040 1457.282    0.000 6650.478    0.001 _functional.py:53(adam)
              370552000 1041.297    0.000 6626.710    0.000 layers.py:465(check)
                7381016  182.124    0.000 5281.401    0.001 agent.py:49(__call__)
                3705520 1974.283    0.001 4550.316    0.001 agent.py:86(interveen)
                3705521  379.891    0.000 4549.066    0.001 layers.py:419(update)
                3705520 2449.689    0.001 4517.347    0.001 replaybuffer.py:28(teleporter_save_data)
                7411040   31.647    0.000 4436.310    0.001 tensor.py:195(backward)
                3705520 3096.877    0.001 4434.239    0.001 replaybuffer.py:22(sample_data)
                7411040   28.343    0.000 4403.476    0.001 __init__.py:68(backward)
                7411040 4211.077    0.001 4211.077    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              370552000  592.827    0.000 2963.953    0.000 layers.py:459(isFree)
               36995152   83.364    0.000 2852.178    0.000 conv.py:398(forward)
                3705520 1636.085    0.000 2767.503    0.001 agent.py:67(modify)
               36995152   53.434    0.000 2734.718    0.000 conv.py:390(_conv_forward)
               36995152 2681.285    0.000 2681.285    0.000 {built-in method conv2d}
               37055210 1454.369    0.000 2413.014    0.000 layer.py:129(update)
             3128587107 1917.683    0.000 2371.127    0.000 layer.py:81(isFree)
               48081688  105.196    0.000 2218.968    0.000 linear.py:93(forward)
               48081688   39.764    0.000 2068.759    0.000 functional.py:1737(linear)
               48081688 2018.218    0.000 2018.218    0.000 {built-in method torch._C._nn.linear}
              139500644 1739.295    0.000 1739.295    0.000 {built-in method clone}
                3705520   54.751    0.000 1689.089    0.000 agent.py:110(__call__)
               11086536   79.512    0.000 1586.200    0.000 agent.py:59(modify_board)
             6292111120 1050.569    0.000 1482.601    0.000 enum.py:646(__hash__)
              133398720 1342.849    0.000 1342.849    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33319656 1339.910    0.000 1339.910    0.000 {built-in method cat}
               15895449 1312.632    0.000 1312.632    0.000 {built-in method tensor}
               66579264   54.239    0.000 1243.451    0.000 activation.py:713(forward)
              133398720 1197.924    0.000 1197.924    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               66579264   55.896    0.000 1189.212    0.000 functional.py:1364(leaky_relu)
              370552000  765.377    0.000 1186.847    0.000 layers.py:270(check)
               66579264 1121.155    0.000 1121.155    0.000 {built-in method torch._C._nn.leaky_relu}
              370552000  664.227    0.000 1086.176    0.000 layers.py:233(check)
                3705520   69.834    0.000 1077.031    0.000 replaybuffer.py:18(stacker)
                7411040    9.345    0.000 1049.432    0.000 game.py:31(board)
                7411040  170.967    0.000 1045.603    0.000 optimizer.py:189(zero_grad)
               11086536 1009.020    0.000 1009.020    0.000 {built-in method torch._C._nn.one_hot}
              370552000  759.335    0.000  978.700    0.000 layers.py:67(check)
                2744420   28.853    0.000  883.975    0.000 layers.py:469(restart)
                3705520  449.077    0.000  744.706    0.000 collector.py:54(collect)
               66699360  741.031    0.000  741.031    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              370552100   64.964    0.000  734.660    0.000 {built-in method builtins.all}
             8786233095  734.350    0.000  734.350    0.000 layer.py:77(positions)
              745168939  139.142    0.000  709.374    0.000 layers.py:425(<genexpr>)
               66699360  651.507    0.000  651.507    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              370552000  473.913    0.000  628.298    0.000 layers.py:56(check)
               66699360  622.585    0.000  622.585    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               66699360  618.414    0.000  618.414    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2744420   15.170    0.000  608.526    0.000 level.py:8(__init__)
              370552000  384.067    0.000  595.422    0.000 layers.py:294(check)
              370552100  383.543    0.000  569.620    0.000 layers.py:100(isDone)
             1050479492  569.077    0.000  569.077    0.000 layer.py:124(elements)
              370552000  355.613    0.000  554.519    0.000 layers.py:257(check)
                7381016  197.425    0.000  548.691    0.000 exploration.py:53(softmaxer)
                2744420   86.487    0.000  482.271    0.000 levels.py:199(generate)
               66699360  474.199    0.000  474.199    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              370552000  315.942    0.000  464.209    0.000 layers.py:42(check)
              150587180  460.007    0.000  460.007    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             6292138159  432.037    0.000  432.037    0.000 {built-in method builtins.hash}
              466895574  311.186    0.000  387.062    0.000 tensor.py:906(grad)
        4727412764/4727412762  313.687    0.000  367.299    0.000 {built-in method builtins.len}
                7411040   11.295    0.000  363.320    0.000 loss.py:527(forward)
                7411040   28.079    0.000  352.025    0.000 functional.py:2898(mse_loss)
               22233120  311.979    0.000  311.979    0.000 {built-in method sum}
                5488840   38.099    0.000  311.292    0.000 level.py:41(notUsed)
                9194360  107.770    0.000  295.357    0.000 random.py:315(sample)
              488671142  192.390    0.000  261.443    0.000 layer.py:108(add)
             2525870422  260.193    0.000  260.193    0.000 layer.py:181(isBlocking)
               27444200   34.752    0.000  238.125    0.000 layer.py:58(restart)
              323308952  157.176    0.000  235.038    0.000 layer.py:104(remove)
                7411040  231.998    0.000  231.998    0.000 {built-in method torch._C._nn.mse_loss}
               36995152   25.938    0.000  212.889    0.000 flatten.py:39(forward)
                3705520   18.465    0.000  210.947    0.000 exploration.py:47(epsilonGreedy)
               11116560   18.990    0.000  207.043    0.000 tensor.py:525(__rsub__)
                7412148  204.729    0.000  204.729    0.000 {built-in method max}
               36995152  186.950    0.000  186.950    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11116560  185.108    0.000  185.108    0.000 {built-in method rsub}
                7381016  179.574    0.000  179.574    0.000 {built-in method multinomial}
              259772651  113.739    0.000  165.717    0.000 random.py:250(_randbelow_with_getrandbits)
              236764444  160.412    0.000  160.412    0.000 {built-in method torch._C._get_tracing_state}
                7411040  159.393    0.000  159.393    0.000 {built-in method gather}
                7411040   28.777    0.000  157.936    0.000 __init__.py:28(_make_grads)
               14822080   34.140    0.000  156.262    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9495295: <causal4_teleport_0> in cluster <dcc> Done

Job <causal4_teleport_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:27 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 10:51:00 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 10:51:00 2021
Terminated at Tue Apr  6 02:46:21 2021
Results reported at Tue Apr  6 02:46:21 2021

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

    CPU time :                                   57162.32 sec.
    Max Memory :                                 7711 MB
    Average Memory :                             5325.64 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8673.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57322 sec.
    Turnaround time :                            86934 sec.

The output (if any) is above this job summary.

