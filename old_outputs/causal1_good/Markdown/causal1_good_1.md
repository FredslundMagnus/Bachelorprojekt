
# Parameters

    Name :                      causal1_good-1
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     20.0
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
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1195 minutes.
    Hours used :                19 hours.

# Profiling


      54622191744 function calls (54402690861 primitive calls) in 71710.79 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71710.794 71710.794 {built-in method builtins.exec}
                      1    2.002    2.002 71710.794 71710.794 <string>:1(<module>)
                      1  187.208  187.208 71708.792 71708.792 main.py:43(teleport)
                7839708   27.914    0.000 22316.888    0.003 agent.py:27(learn)
                7839708  578.268    0.000 18853.193    0.002 learner.py:42(Qlearn)
                3919854   16.466    0.000 15601.093    0.004 game.py:27(step)
                3919854   21.797    0.000 14719.034    0.004 layers.py:475(step)
                3919854 7746.729    0.002 14058.960    0.004 replaybuffer.py:29(teleporter_save_data)
                3919854  412.941    0.000 13473.636    0.003 agent.py:52(_learn)
        246937854/27437982  999.472    0.000 9049.290    0.000 module.py:866(_call_impl)
                3919854  112.957    0.000 8799.363    0.002 agent.py:113(_learn)
                3919854 5799.897    0.001 8564.434    0.002 agent.py:84(interveen)
               19598274   56.970    0.000 8428.236    0.000 network.py:24(forward)
                3919854  295.002    0.000 8272.321    0.002 layers.py:18(step)
               19598274  266.000    0.000 8248.241    0.000 container.py:117(forward)
              391985400  488.238    0.000 7944.362    0.000 layer.py:76(move)
                7839708   68.810    0.000 7871.739    0.001 optimizer.py:84(wrapper)
                7839708   32.830    0.000 7552.032    0.001 grad_mode.py:24(decorate_context)
                7839708  216.752    0.000 7444.615    0.001 adam.py:55(step)
                7839708 1540.676    0.000 6968.266    0.001 _functional.py:53(adam)
                3919855  407.864    0.000 6397.460    0.002 layers.py:446(update)
                7838712  194.405    0.000 5637.103    0.001 agent.py:47(__call__)
              433691268 5059.828    0.000 5059.828    0.000 {built-in method clone}
                3919854 3354.200    0.001 4747.248    0.001 replaybuffer.py:23(sample_data)
                7839708   34.142    0.000 4732.435    0.001 tensor.py:195(backward)
                7839708   31.470    0.000 4697.083    0.001 __init__.py:68(backward)
              391985400  813.727    0.000 4528.839    0.000 layers.py:492(check)
                7839708 4493.136    0.001 4493.136    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3919854 2001.136    0.001 3178.104    0.001 agent.py:65(modify)
               39196548   86.175    0.000 3034.738    0.000 conv.py:398(forward)
               39196548   49.880    0.000 2912.100    0.000 conv.py:390(_conv_forward)
               39196548 2862.220    0.000 2862.220    0.000 {built-in method conv2d}
               13676642  109.298    0.000 2815.473    0.000 layers.py:496(restart)
              391985400  585.330    0.000 2452.945    0.000 layers.py:486(isFree)
               50955114  103.672    0.000 2353.763    0.000 linear.py:93(forward)
               50955114   42.187    0.000 2199.509    0.000 functional.py:1737(linear)
               50955114 2147.359    0.000 2147.359    0.000 {built-in method torch._C._nn.linear}
               31358840 1169.485    0.000 2021.993    0.000 layer.py:137(NoRock_update)
             3046534920 1475.871    0.000 1867.614    0.000 layer.py:73(isFree)
               13676642   52.236    0.000 1818.675    0.000 level.py:8(__init__)
                3919854   58.128    0.000 1787.463    0.000 agent.py:108(__call__)
               11758566   80.021    0.000 1706.346    0.000 agent.py:57(modify_board)
               13676642  101.619    0.000 1542.210    0.000 levels.py:122(generate)
              141114744 1418.061    0.000 1418.061    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               35277690 1389.660    0.000 1389.660    0.000 {built-in method cat}
              445449834 1360.487    0.000 1360.487    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             6029090595  957.176    0.000 1357.420    0.000 enum.py:646(__hash__)
               41029926  307.569    0.000 1343.198    0.000 level.py:41(notUsed)
               70553388   54.921    0.000 1313.963    0.000 activation.py:713(forward)
               70553388   58.787    0.000 1259.042    0.000 functional.py:1364(leaky_relu)
              141114744 1252.486    0.000 1252.486    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16796528 1244.683    0.000 1244.683    0.000 {built-in method tensor}
               70553388 1188.289    0.000 1188.289    0.000 {built-in method torch._C._nn.leaky_relu}
                3919854   73.442    0.000 1112.922    0.000 replaybuffer.py:19(stacker)
                7839708  179.145    0.000 1112.224    0.000 optimizer.py:189(zero_grad)
               11758566 1101.525    0.000 1101.525    0.000 {built-in method torch._C._nn.one_hot}
              391985500  114.121    0.000 1003.204    0.000 {built-in method builtins.all}
              391985400  617.264    0.000  978.196    0.000 layers.py:302(check)
                7839708    9.534    0.000  966.804    0.000 game.py:23(board)
             1261153065  288.513    0.000  933.555    0.000 layers.py:452(<genexpr>)
              391985400  572.832    0.000  923.656    0.000 layers.py:261(check)
              109413136   76.604    0.000  852.781    0.000 layer.py:50(restart)
                3919854  480.638    0.000  794.932    0.000 collector.py:54(collect)
               70557372  775.036    0.000  775.036    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               70557372  678.975    0.000  678.975    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13676742  325.003    0.000  651.636    0.000 layers.py:33(reset)
               70557372  647.835    0.000  647.835    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              391985400  419.811    0.000  641.515    0.000 layers.py:328(check)
               70557372  634.568    0.000  634.568    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              391985500  402.240    0.000  600.878    0.000 layers.py:110(isDone)
                7838712  213.940    0.000  584.130    0.000 exploration.py:53(softmaxer)
              391985400  362.880    0.000  568.608    0.000 layers.py:287(check)
             6299066700  554.110    0.000  554.110    0.000 layer.py:69(positions)
             1762158945  547.585    0.000  547.585    0.000 layer.py:116(elements)
               41029926   28.118    0.000  509.874    0.000 level.py:38(elementsIn)
              391985400  321.418    0.000  509.827    0.000 layers.py:47(check)
               70557372  497.130    0.000  497.130    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              856538443  316.123    0.000  439.403    0.000 layer.py:100(add)
              493901658  350.668    0.000  432.507    0.000 tensor.py:906(grad)
             6029119146  400.248    0.000  400.248    0.000 {built-in method builtins.hash}
                7839708   11.822    0.000  381.779    0.000 loss.py:527(forward)
                7839708   28.962    0.000  369.957    0.000 functional.py:2898(mse_loss)
             2013203548  364.332    0.000  364.332    0.000 level.py:32(inverse)
               23519124  333.497    0.000  333.497    0.000 {built-in method sum}
        3523654784/3523654782  261.676    0.000  319.494    0.000 {built-in method builtins.len}
               41029926  160.634    0.000  313.049    0.000 level.py:39(<listcomp>)
                3919854   97.145    0.000  272.600    0.000 random.py:315(sample)
              391356732  178.727    0.000  264.657    0.000 layer.py:96(remove)
                7839708  242.202    0.000  242.202    0.000 {built-in method torch._C._nn.mse_loss}
               39196548   25.839    0.000  222.697    0.000 flatten.py:39(forward)
                7840882  217.277    0.000  217.277    0.000 {built-in method max}
               11759562   17.221    0.000  215.505    0.000 tensor.py:525(__rsub__)
             2288092200  214.965    0.000  214.965    0.000 layer.py:177(isBlocking)
                3919854   18.294    0.000  214.080    0.000 exploration.py:47(epsilonGreedy)
               39196548  196.858    0.000  196.858    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11759562  195.222    0.000  195.222    0.000 {built-in method rsub}
             2504803729  191.893    0.000  191.893    0.000 {method 'append' of 'list' objects}
               13676642   86.783    0.000  191.580    0.000 level.py:16(<dictcomp>)
                7838712  187.589    0.000  187.589    0.000 {built-in method multinomial}
             1039424799  179.848    0.000  179.848    0.000 enum.py:352(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9474222: <causal1_good_1> in cluster <dcc> Done

Job <causal1_good_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 27 17:45:03 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 17:45:04 2021
Terminated at Sun Mar 28 14:40:22 2021
Results reported at Sun Mar 28 14:40:22 2021

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

    CPU time :                                   71531.55 sec.
    Max Memory :                                 8000 MB
    Average Memory :                             5570.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8384.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71735 sec.
    Turnaround time :                            71719 sec.

The output (if any) is above this job summary.

