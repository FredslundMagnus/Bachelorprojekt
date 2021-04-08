
# Parameters

    Name :                      causal3_demo-0
    Main :                      teleport
    Level :                     Levels.Causal3
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
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      47090598044 function calls (46922130269 primitive calls) in 57319.65 seconds

##    Ordered by: cumulative time
   List reduced from 478 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57319.649 57319.649 {built-in method builtins.exec}
                      1    1.838    1.838 57319.649 57319.649 <string>:1(<module>)
                      1  140.160  140.160 57317.811 57317.811 main.py:40(teleport)
                6018264   21.310    0.000 21481.351    0.004 agent.py:29(learn)
                6018264  514.161    0.000 18401.790    0.003 learner.py:42(Qlearn)
                3009132   14.383    0.000 13467.772    0.004 game.py:41(step)
                3009132  104.188    0.000 12920.254    0.004 agent.py:54(_learn)
                3009132   16.343    0.000 12738.298    0.004 layers.py:710(step)
                3009132   85.493    0.000 8528.240    0.003 agent.py:117(_learn)
        189526969/21060205  779.874    0.000 8419.925    0.000 module.py:715(_call_impl)
               15041941   38.349    0.000 7891.537    0.001 network.py:24(forward)
                6018264   35.948    0.000 7861.193    0.001 grad_mode.py:23(decorate_context)
               15041941  202.542    0.000 7767.310    0.001 container.py:115(forward)
                6018264  207.335    0.000 7755.194    0.001 adam.py:55(step)
                3009132  239.404    0.000 7320.634    0.002 layers.py:17(step)
              300913200  512.108    0.000 7051.452    0.000 layer.py:98(move)
                3009132 3500.539    0.001 6772.443    0.002 replaybuffer.py:28(teleporter_save_data)
                6018264 1434.487    0.000 6679.287    0.001 functional.py:53(adam)
                3009132 2916.856    0.001 5478.992    0.002 agent.py:88(interveen)
                3009133  434.706    0.000 5381.410    0.002 layers.py:676(update)
                6014545  142.609    0.000 5147.141    0.001 agent.py:49(__call__)
                6018264   38.797    0.000 4165.671    0.001 tensor.py:181(backward)
                6018264   20.601    0.000 4126.875    0.001 __init__.py:68(backward)
              300913200  726.870    0.000 4065.698    0.000 layers.py:727(check)
                6018264 3946.087    0.001 3946.087    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3009132 2309.752    0.001 3880.492    0.001 replaybuffer.py:22(sample_data)
                3009132 1749.910    0.001 3353.818    0.001 agent.py:67(modify)
               30083882   53.902    0.000 2792.621    0.000 conv.py:422(forward)
               30083882   58.053    0.000 2718.629    0.000 conv.py:414(_conv_forward)
               30083882 2650.235    0.000 2650.235    0.000 {built-in method conv2d}
              177018450 2579.964    0.000 2579.964    0.000 {built-in method clone}
               39107559   91.898    0.000 2528.017    0.000 linear.py:92(forward)
               39107559  156.220    0.000 2396.374    0.000 functional.py:1669(linear)
              300913200  430.280    0.000 2047.297    0.000 layers.py:721(isFree)
               39107559 1710.789    0.000 1710.789    0.000 {built-in method addmm}
              842458836  473.770    0.000 1646.034    0.000 {built-in method builtins.any}
               27078469 1638.471    0.000 1638.471    0.000 {built-in method cat}
              379150686 1045.781    0.000 1636.990    0.000 tensor.py:933(grad)
                3009132   41.044    0.000 1623.178    0.001 agent.py:112(__call__)
             2066631167 1300.393    0.000 1617.018    0.000 layer.py:95(isFree)
                6018264  157.289    0.000 1598.467    0.000 optimizer.py:167(zero_grad)
                9023677   65.641    0.000 1523.097    0.000 agent.py:59(modify_board)
               24073064  836.070    0.000 1481.226    0.000 layer.py:167(NoRock_update)
              108328752 1389.055    0.000 1389.055    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3009132   58.179    0.000 1354.549    0.000 replaybuffer.py:18(stacker)
              321979034  186.731    0.000 1239.491    0.000 {built-in method builtins.all}
              108328752 1180.354    0.000 1180.354    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               54149500   52.575    0.000 1172.339    0.000 activation.py:713(forward)
               54149500   72.504    0.000 1119.764    0.000 functional.py:1292(leaky_relu)
             4491313596  778.214    0.000 1116.797    0.000 enum.py:646(__hash__)
             1812810219  482.275    0.000 1075.283    0.000 layers.py:682(<genexpr>)
               54149500 1040.037    0.000 1040.037    0.000 {built-in method torch._C._nn.leaky_relu}
              300913200  638.210    0.000 1017.896    0.000 layers.py:240(check)
               12969236 1006.210    0.000 1006.210    0.000 {built-in method tensor}
                3086396   28.644    0.000  987.555    0.000 layers.py:731(restart)
                9023677  950.212    0.000  950.212    0.000 {built-in method torch._C._nn.one_hot}
              300913200  573.504    0.000  943.400    0.000 layers.py:280(check)
             2680442136  727.131    0.000  877.217    0.000 layers.py:692(<genexpr>)
               21065734  119.776    0.000  824.897    0.000 tensor.py:21(wrapped)
              186042127  809.276    0.000  809.276    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              493487844  280.792    0.000  806.925    0.000 overrides.py:1070(has_torch_function)
               54164376  762.292    0.000  762.292    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6018264    8.161    0.000  758.797    0.000 game.py:37(board)
                3009132  442.350    0.000  744.070    0.000 collector.py:53(collect)
                3086396   14.798    0.000  706.559    0.000 level.py:8(__init__)
               54164376  698.914    0.000  698.914    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               54164376  630.246    0.000  630.246    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54164376  565.823    0.000  565.823    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6014545  195.014    0.000  546.729    0.000 exploration.py:53(softmaxer)
                3086396   62.448    0.000  541.919    0.000 levels.py:164(generate)
              300913300  339.479    0.000  514.332    0.000 layers.py:107(isDone)
             5210947933  473.771    0.000  473.771    0.000 layer.py:91(positions)
              300913200  289.114    0.000  458.595    0.000 layers.py:267(check)
              300913200  280.255    0.000  448.410    0.000 layers.py:307(check)
               54164376  447.480    0.000  447.480    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6172792   56.530    0.000  391.839    0.000 level.py:41(notUsed)
              300913200  261.217    0.000  391.285    0.000 layers.py:42(check)
              903591925  378.277    0.000  378.277    0.000 layer.py:146(elements)
                6018264    9.033    0.000  351.037    0.000 loss.py:445(forward)
               15045660  346.723    0.000  346.723    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               39107559  345.211    0.000  345.211    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6018264   32.354    0.000  342.004    0.000 functional.py:2637(mse_loss)
             4491335595  338.587    0.000  338.587    0.000 {built-in method builtins.hash}
        2831832723/2831832721  212.208    0.000  307.038    0.000 {built-in method builtins.len}
               18054792  297.753    0.000  297.753    0.000 {built-in method sum}
             1047148380  231.849    0.000  291.144    0.000 overrides.py:1083(<genexpr>)
                9181924  102.954    0.000  273.575    0.000 random.py:315(sample)
               24691168   29.769    0.000  243.913    0.000 layer.py:69(restart)
              428827082  175.810    0.000  236.470    0.000 layer.py:130(add)
               30083882   21.973    0.000  217.976    0.000 flatten.py:39(forward)
                6018264  216.283    0.000  216.283    0.000 {built-in method torch._C._nn.mse_loss}
              271378632  131.209    0.000  197.082    0.000 layer.py:126(remove)
               30083882  196.003    0.000  196.003    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6019165  194.888    0.000  194.888    0.000 {built-in method max}
                3010334  191.627    0.000  191.627    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                6014545  177.065    0.000  177.065    0.000 {built-in method multinomial}
              192537303  172.630    0.000  172.630    0.000 {built-in method torch._C._get_tracing_state}
                3009132   11.794    0.000  171.422    0.000 exploration.py:47(epsilonGreedy)
             1559470634  163.649    0.000  163.649    0.000 layer.py:203(isBlocking)
                6018264  160.201    0.000  160.201    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 9501897: <causal3_demo_0> in cluster <dcc> Done

Job <causal3_demo_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Wed Apr  7 16:17:45 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 06:46:48 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 06:46:48 2021
Terminated at Thu Apr  8 22:42:16 2021
Results reported at Thu Apr  8 22:42:16 2021

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

    CPU time :                                   57165.94 sec.
    Max Memory :                                 2815 MB
    Average Memory :                             2807.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13569.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57328 sec.
    Turnaround time :                            109471 sec.

The output (if any) is above this job summary.

