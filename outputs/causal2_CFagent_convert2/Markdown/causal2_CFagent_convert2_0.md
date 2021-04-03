
# Parameters

    Name :                      causal2_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal2
    Hours :                     13.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
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
    Cf convert :                1
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      28159324976 function calls (27970342569 primitive calls) in 46515.26 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46515.265 46515.265 {built-in method builtins.exec}
                      1    5.329    5.329 46515.265 46515.265 <string>:1(<module>)
                      1  176.047  176.047 46509.935 46509.935 main.py:96(CFagent)
                6193539   27.507    0.000 15544.689    0.003 agent.py:28(learn)
                6193539  395.459    0.000 12567.313    0.002 learner.py:42(Qlearn)
                2064513   10.987    0.000 7754.481    0.004 game.py:36(step)
                2064513   13.667    0.000 7321.284    0.004 layers.py:594(step)
        211610819/22630103  897.464    0.000 7082.498    0.000 module.py:866(_call_impl)
               16436564   42.889    0.000 6602.272    0.000 network.py:24(forward)
               16436564  217.400    0.000 6440.638    0.000 container.py:117(forward)
                2064513  240.538    0.000 6065.174    0.003 agent.py:53(_learn)
                2064513  238.096    0.000 5529.394    0.003 agent.py:189(_learn)
                6193539   56.275    0.000 4822.970    0.001 optimizer.py:84(wrapper)
                2064513  203.224    0.000 4785.042    0.002 layers.py:18(step)
                2064513 2824.922    0.001 4764.315    0.002 replaybuffer.py:28(teleporter_save_data)
                6193539   32.117    0.000 4580.828    0.001 grad_mode.py:24(decorate_context)
              206326744  268.441    0.000 4561.693    0.000 layer.py:82(move)
                6193539  209.336    0.000 4482.611    0.001 adam.py:55(step)
                2064513  342.194    0.000 4366.982    0.002 agent.py:197(counterfact)
                6193539  944.781    0.000 4056.097    0.001 _functional.py:53(adam)
                2064513 3266.185    0.002 4022.296    0.002 replaybuffer.py:22(sample_data)
                2064513   69.008    0.000 3908.494    0.002 agent.py:114(_learn)
                5121084  155.109    0.000 3411.682    0.001 agent.py:48(__call__)
                2064513 2022.947    0.001 3373.745    0.002 agent.py:85(interveen)
                2064513 2696.389    0.001 3355.712    0.002 replaybuffer.py:49(sample_data)
                6193539   27.192    0.000 3332.168    0.001 tensor.py:195(backward)
                6193539   28.084    0.000 3304.083    0.001 __init__.py:68(backward)
                6193539 3150.998    0.001 3150.998    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              206326744  408.664    0.000 2506.098    0.000 layers.py:611(check)
                2064514  226.551    0.000 2498.832    0.001 layers.py:565(update)
               32873128   75.944    0.000 2389.009    0.000 conv.py:398(forward)
               32873128   51.001    0.000 2273.378    0.000 conv.py:390(_conv_forward)
               32873128 2222.377    0.000 2222.377    0.000 {built-in method conv2d}
               28903189 1210.458    0.000 2140.655    0.000 layer.py:143(NoRock_update)
               26773419 2108.250    0.000 2108.250    0.000 {built-in method tensor}
               21005692   15.970    0.000 1950.738    0.000 game.py:32(board)
               45180666   92.882    0.000 1808.087    0.000 linear.py:93(forward)
              180232512 1718.116    0.000 1718.116    0.000 {built-in method clone}
               45180666   39.491    0.000 1664.413    0.000 functional.py:1737(linear)
               45180666 1615.613    0.000 1615.613    0.000 {built-in method torch._C._nn.linear}
              206227230  286.318    0.000 1502.274    0.000 layers.py:605(isFree)
                2064513  826.149    0.000 1380.371    0.001 agent.py:66(modify)
             1369201338 1048.339    0.000 1215.956    0.000 layer.py:79(isFree)
                 992915    9.980    0.000 1178.784    0.001 agent.py:167(choose_action)
               29895240 1149.842    0.000 1149.842    0.000 {built-in method cat}
               61617230   56.031    0.000  958.691    0.000 activation.py:713(forward)
                2064513   43.294    0.000  957.330    0.000 agent.py:163(__call__)
                7185597   46.530    0.000  945.680    0.000 agent.py:58(modify_board)
                2064513   41.375    0.000  906.227    0.000 agent.py:109(__call__)
               61617230   52.688    0.000  902.660    0.000 functional.py:1364(leaky_relu)
               61617230  840.163    0.000  840.163    0.000 {built-in method torch._C._nn.leaky_relu}
              115612728  788.429    0.000  788.429    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6193539  133.555    0.000  712.891    0.000 optimizer.py:189(zero_grad)
              115612728  696.707    0.000  696.707    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2506034411  441.553    0.000  636.331    0.000 enum.py:646(__hash__)
                7185597  627.581    0.000  627.581    0.000 {built-in method torch._C._nn.one_hot}
                2064513   52.298    0.000  588.950    0.000 replaybuffer.py:18(stacker)
              206326744  363.085    0.000  585.617    0.000 layers.py:231(check)
              206326744  372.857    0.000  582.366    0.000 layers.py:245(check)
              206326744  370.580    0.000  579.279    0.000 layers.py:217(check)
              206451400   59.963    0.000  573.110    0.000 {built-in method builtins.all}
              549577797  561.072    0.000  561.072    0.000 layer.py:122(elements)
              644456878  154.476    0.000  537.190    0.000 layers.py:571(<genexpr>)
                1432162   16.844    0.000  528.204    0.000 layers.py:615(restart)
                2064513   45.455    0.000  500.692    0.000 replaybuffer.py:45(stacker)
               57806364  461.925    0.000  461.925    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               57806364  411.807    0.000  411.807    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1432162    9.470    0.000  401.602    0.000 level.py:8(__init__)
              189482622  371.357    0.000  371.357    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               57806364  369.066    0.000  369.066    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               57806364  368.148    0.000  368.148    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              206451400  251.543    0.000  360.960    0.000 layers.py:111(isDone)
                2064513  139.204    0.000  359.317    0.000 replaybuffer.py:55(CF_save_data)
                5121084  128.094    0.000  353.106    0.000 exploration.py:53(softmaxer)
              404644632  272.998    0.000  336.765    0.000 tensor.py:906(grad)
                1432162   19.126    0.000  332.508    0.000 levels.py:151(generate)
                4129026  121.685    0.000  318.186    0.000 random.py:315(sample)
             3498783524  316.297    0.000  316.297    0.000 layer.py:75(positions)
                2064513  186.555    0.000  315.735    0.000 collector.py:54(collect)
        3859079949/3859079946  260.424    0.000  299.071    0.000 {built-in method builtins.len}
              206326744  202.530    0.000  297.244    0.000 layers.py:204(check)
                6874727   61.948    0.000  294.576    0.000 level.py:41(notUsed)
                6193539   11.087    0.000  284.407    0.000 loss.py:527(forward)
               57806364  275.282    0.000  275.282    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6193539   29.719    0.000  273.320    0.000 functional.py:2898(mse_loss)
                6193540  260.163    0.000  260.163    0.000 {built-in method nonzero}
                3057428   17.355    0.000  248.632    0.000 exploration.py:47(epsilonGreedy)
             2506058186  194.782    0.000  194.782    0.000 {built-in method builtins.hash}
              196863985  118.712    0.000  173.299    0.000 layer.py:102(remove)
                6193539  164.374    0.000  164.374    0.000 {built-in method torch._C._nn.mse_loss}
              246536129  114.348    0.000  156.940    0.000 layer.py:106(add)
               32873128   23.772    0.000  155.005    0.000 flatten.py:39(forward)
                6194356  150.833    0.000  150.833    0.000 {built-in method max}
              213390134   92.318    0.000  138.098    0.000 random.py:250(_randbelow_with_getrandbits)
               12387078  135.771    0.000  135.771    0.000 {built-in method sum}
             1369201338  134.959    0.000  134.959    0.000 layer.py:183(isBlocking)
               32873128  131.233    0.000  131.233    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               28903189  129.791    0.000  129.791    0.000 layer.py:154(<listcomp>)
                1627165   60.012    0.000  129.589    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                8258052   13.916    0.000  129.449    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9493318: <causal2_CFagent_convert2_0> in cluster <dcc> Done

Job <causal2_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:08 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:19:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:19:52 2021
Terminated at Sat Apr  3 11:15:15 2021
Results reported at Sat Apr  3 11:15:15 2021

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

    CPU time :                                   46400.76 sec.
    Max Memory :                                 7130 MB
    Average Memory :                             5248.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9254.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46523 sec.
    Turnaround time :                            47107 sec.

The output (if any) is above this job summary.

