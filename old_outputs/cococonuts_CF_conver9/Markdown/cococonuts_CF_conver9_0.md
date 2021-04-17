
# Parameters

    Name :                      cococonuts_CF_conver9-0
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
    Cf convert :                9
    Counterfacts :              1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      72276167490 function calls (71917096483 primitive calls) in 86113.72 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.722 86113.722 {built-in method builtins.exec}
                      1    4.383    4.383 86113.722 86113.722 <string>:1(<module>)
                      1  281.515  281.515 86109.339 86109.339 main.py:94(CFagent)
               12286827   47.913    0.000 28749.246    0.002 agent.py:29(learn)
               12286817  716.502    0.000 23409.448    0.002 learner.py:42(Qlearn)
                4095609   20.238    0.000 23123.567    0.006 game.py:41(step)
                4095609   23.013    0.000 22306.289    0.005 layers.py:710(step)
                4095609  395.511    0.000 15073.207    0.004 layers.py:17(step)
              408966738 1545.071    0.000 14638.184    0.000 layer.py:98(move)
        402643779/43574463 1586.977    0.000 12522.263    0.000 module.py:866(_call_impl)
               31287646   83.052    0.000 11657.974    0.000 network.py:24(forward)
               31287646  368.236    0.000 11375.673    0.000 container.py:117(forward)
                4095609  409.406    0.000 11154.533    0.003 agent.py:54(_learn)
                4095609  406.269    0.000 10260.417    0.003 agent.py:208(_learn)
               12286817  100.388    0.000 9050.655    0.001 optimizer.py:84(wrapper)
              408966738 1043.695    0.000 8656.357    0.000 layers.py:727(check)
               12286817   51.780    0.000 8592.594    0.001 grad_mode.py:24(decorate_context)
               12286817  366.420    0.000 8424.029    0.001 adam.py:55(step)
               12286817 1731.254    0.000 7653.882    0.001 _functional.py:53(adam)
                4095609  114.226    0.000 7255.724    0.002 agent.py:117(_learn)
                4095610  592.721    0.000 7170.708    0.002 layers.py:676(update)
                4095609  509.459    0.000 7164.962    0.002 agent.py:216(counterfact)
               12286817   58.899    0.000 6280.756    0.001 tensor.py:195(backward)
               12286817   47.783    0.000 6220.210    0.001 __init__.py:68(backward)
                4095609 4898.306    0.001 6206.163    0.002 replaybuffer.py:22(sample_data)
               12286817 5938.261    0.000 5938.261    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9486450  225.315    0.000 5818.272    0.001 agent.py:49(__call__)
                4095609 4175.239    0.001 5335.441    0.001 replaybuffer.py:49(sample_data)
                4095609 2706.766    0.001 4748.205    0.001 replaybuffer.py:28(teleporter_save_data)
                4095609 2065.707    0.001 4538.793    0.001 agent.py:88(interveen)
               62575292  135.991    0.000 4238.391    0.000 conv.py:398(forward)
               62575292   92.145    0.000 4035.487    0.000 conv.py:390(_conv_forward)
               62575292 3943.342    0.000 3943.342    0.000 {built-in method conv2d}
               57338533 2285.713    0.000 3925.484    0.000 layer.py:151(update)
               49502531 3801.777    0.000 3801.777    0.000 {built-in method tensor}
               40148412   25.592    0.000 3580.252    0.000 game.py:37(board)
              408765384  596.505    0.000 3475.083    0.000 layers.py:721(isFree)
              408966738 2559.861    0.000 3464.831    0.000 layers.py:464(check)
               85671720  172.257    0.000 3193.732    0.000 linear.py:93(forward)
               85671720   68.032    0.000 2932.481    0.000 functional.py:1737(linear)
             2759612602 2490.002    0.000 2878.578    0.000 layer.py:95(isFree)
               85671720 2847.562    0.000 2847.562    0.000 {built-in method torch._C._nn.linear}
                4095609 1853.409    0.000 2824.317    0.001 agent.py:67(modify)
              408966738 1775.536    0.000 2403.622    0.000 layers.py:71(check)
               58633708 2000.336    0.000 2000.336    0.000 {built-in method cat}
              203143978 1872.931    0.000 1872.931    0.000 {built-in method clone}
             7694657558 1316.827    0.000 1842.397    0.000 enum.py:646(__hash__)
                1964760   24.489    0.000 1782.384    0.001 layers.py:731(restart)
                4095599   68.421    0.000 1758.566    0.000 agent.py:167(__call__)
               13582059   87.517    0.000 1678.719    0.000 agent.py:59(modify_board)
                4095609   65.021    0.000 1673.479    0.000 agent.py:112(__call__)
              116959366   92.164    0.000 1659.948    0.000 activation.py:713(forward)
                1323171   27.807    0.000 1656.132    0.001 agent.py:171(choose_action)
              116959366   91.820    0.000 1567.784    0.000 functional.py:1364(leaky_relu)
                1964760   11.539    0.000 1562.296    0.001 level.py:8(__init__)
              229353904 1488.418    0.000 1488.418    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              116959366 1457.498    0.000 1457.498    0.000 {built-in method torch._C._nn.leaky_relu}
                1964760   92.459    0.000 1445.763    0.001 levels.py:262(generate)
              411691850  316.176    0.000 1352.055    0.000 {built-in method builtins.any}
               12286817  231.039    0.000 1328.543    0.000 optimizer.py:189(zero_grad)
              229353904 1315.180    0.000 1315.180    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               24318472  209.517    0.000 1268.755    0.000 level.py:41(notUsed)
              409561000  110.311    0.000 1122.078    0.000 {built-in method builtins.all}
               13582059 1102.806    0.000 1102.806    0.000 {built-in method torch._C._nn.one_hot}
              408966738  859.742    0.000 1083.951    0.000 layers.py:56(check)
             1246477380  303.106    0.000 1063.517    0.000 layers.py:682(<genexpr>)
             3260769920  846.327    0.000 1035.879    0.000 layers.py:692(<genexpr>)
                4095609   90.634    0.000 1017.126    0.000 replaybuffer.py:18(stacker)
             1157493480  960.534    0.000  960.534    0.000 layer.py:146(elements)
              114676952  933.461    0.000  933.461    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4095599   80.881    0.000  877.454    0.000 replaybuffer.py:45(stacker)
             8756426971  778.220    0.000  778.220    0.000 layer.py:91(positions)
              114676952  761.283    0.000  761.283    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              409561000  492.941    0.000  724.241    0.000 layers.py:107(isDone)
              114676952  697.713    0.000  697.713    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              114676952  697.183    0.000  697.183    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              802738748  506.347    0.000  627.699    0.000 tensor.py:906(grad)
                9486450  218.196    0.000  593.427    0.000 exploration.py:53(softmaxer)
                4095609  349.318    0.000  592.133    0.000 collector.py:53(collect)
               24318472   20.386    0.000  568.381    0.000 level.py:38(elementsIn)
              408966738  386.507    0.000  562.422    0.000 layers.py:42(check)
                8191218  212.612    0.000  558.786    0.000 random.py:315(sample)
        7330464742/7330464739  480.394    0.000  554.024    0.000 {built-in method builtins.len}
              114676952  526.689    0.000  526.689    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7694704069  525.578    0.000  525.578    0.000 {built-in method builtins.hash}
                4095609  171.560    0.000  519.127    0.000 replaybuffer.py:55(CF_save_data)
               12286817   16.890    0.000  507.903    0.000 loss.py:527(forward)
               12286817   46.449    0.000  491.014    0.000 functional.py:2898(mse_loss)
               12286828  464.700    0.000  464.700    0.000 {built-in method nonzero}
              220821636  411.006    0.000  411.006    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              406100436  243.732    0.000  372.701    0.000 layer.py:126(remove)
               24318472  185.200    0.000  365.418    0.000 level.py:39(<listcomp>)
             1084895880  324.165    0.000  324.165    0.000 level.py:32(inverse)
               12286817  300.038    0.000  300.038    0.000 {built-in method torch._C._nn.mse_loss}
              521708185  218.023    0.000  296.044    0.000 layer.py:130(add)
               62575292   44.138    0.000  283.523    0.000 flatten.py:39(forward)
               12288174  270.827    0.000  270.827    0.000 {built-in method max}
                1323171  250.327    0.000  265.471    0.000 agent.py:182(convert_values)
             2759612602  263.071    0.000  263.071    0.000 layer.py:203(isBlocking)
              438280719  175.858    0.000  259.409    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9501863: <cococonuts_CF_conver9_0> in cluster <dcc> Done

Job <cococonuts_CF_conver9_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:07 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 17:07:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 17:07:51 2021
Terminated at Thu Apr  8 17:03:10 2021
Results reported at Thu Apr  8 17:03:10 2021

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

    CPU time :                                   86116.84 sec.
    Max Memory :                                 3574 MB
    Average Memory :                             3535.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12810.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            91023 sec.

The output (if any) is above this job summary.

