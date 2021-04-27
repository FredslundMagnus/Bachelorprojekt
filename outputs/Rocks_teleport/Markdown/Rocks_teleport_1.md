
# Parameters

    Name :                      Rocks_teleport-1
    Main :                      teleport
    Level :                     Levels.Rocks
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67026909851 function calls (66786117428 primitive calls) in 86111.65 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.652 86111.652 {built-in method builtins.exec}
                      1    1.457    1.457 86111.652 86111.652 <string>:1(<module>)
                      1  193.620  193.620 86110.195 86110.195 main.py:45(teleport)
                8601924   32.940    0.000 29350.019    0.003 agent.py:29(learn)
                4300962   17.386    0.000 26161.848    0.006 game.py:41(step)
                4300962   24.437    0.000 25246.784    0.006 layers.py:718(step)
                8601924  699.964    0.000 25119.212    0.003 learner.py:42(Qlearn)
                4300962  141.288    0.000 17645.584    0.004 agent.py:54(_learn)
                4300962  349.529    0.000 15519.729    0.004 layers.py:17(step)
              430096200 1098.559    0.000 15133.561    0.000 layer.py:98(move)
                4300962  115.220    0.000 11654.047    0.003 agent.py:117(_learn)
        270892941/30101529 1010.412    0.000 11407.558    0.000 module.py:715(_call_impl)
              430096200 1152.444    0.000 10807.063    0.000 layers.py:735(check)
                8601924   51.342    0.000 10765.461    0.001 grad_mode.py:23(decorate_context)
               21499605   55.045    0.000 10691.824    0.000 network.py:27(forward)
                8601924  267.644    0.000 10620.289    0.001 adam.py:55(step)
               21499605  271.236    0.000 10511.751    0.000 container.py:115(forward)
                4300963  589.630    0.000 9673.340    0.002 layers.py:684(update)
                8601924 1955.519    0.000 9184.103    0.001 functional.py:53(adam)
                4300962 4494.997    0.001 8636.219    0.002 replaybuffer.py:28(teleporter_save_data)
              430096200 6866.411    0.000 8014.100    0.000 layers.py:77(check)
                4300962 4421.906    0.001 7899.068    0.002 agent.py:88(interveen)
                8596719  195.778    0.000 7016.919    0.001 agent.py:49(__call__)
                8601924   50.466    0.000 5762.165    0.001 tensor.py:181(backward)
                8601924   33.013    0.000 5711.698    0.001 __init__.py:68(backward)
                8601924 5458.065    0.001 5458.065    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4300962 3265.647    0.001 5218.230    0.001 replaybuffer.py:22(sample_data)
                4300962 2775.505    0.001 5000.414    0.001 agent.py:67(modify)
               12515920   93.400    0.000 3951.431    0.000 layers.py:740(restart)
               42999210   73.518    0.000 3817.997    0.000 conv.py:422(forward)
               42999210   81.596    0.000 3716.503    0.000 conv.py:414(_conv_forward)
               42999210 3620.644    0.000 3620.644    0.000 {built-in method conv2d}
               55896891  128.289    0.000 3430.762    0.000 linear.py:92(forward)
              232936214 3292.251    0.000 3292.251    0.000 {built-in method clone}
               55896891  209.999    0.000 3250.315    0.000 functional.py:1669(linear)
               21504815 2000.024    0.000 2818.366    0.000 layer.py:151(update)
               12515920   43.835    0.000 2769.979    0.000 level.py:8(__init__)
              430096200  459.113    0.000 2557.698    0.000 layers.py:729(isFree)
               12515920  303.803    0.000 2359.050    0.000 levels.py:95(generate)
               55896891 2339.298    0.000 2339.298    0.000 {built-in method addmm}
                4300962   60.214    0.000 2217.655    0.001 agent.py:112(__call__)
              541921266 1385.505    0.000 2175.645    0.000 tensor.py:933(grad)
               12897681   92.970    0.000 2110.422    0.000 agent.py:59(modify_board)
                8601924  193.656    0.000 2110.385    0.000 optimizer.py:167(zero_grad)
             2014366646 1806.188    0.000 2098.585    0.000 layer.py:95(isFree)
               34402491 2052.881    0.000 2052.881    0.000 {built-in method cat}
              154834632 1923.060    0.000 1923.060    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1196024666  536.375    0.000 1713.824    0.000 {built-in method builtins.any}
                4300962   76.415    0.000 1668.141    0.000 replaybuffer.py:18(stacker)
              154834632 1633.520    0.000 1633.520    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               77396496   63.567    0.000 1583.864    0.000 activation.py:713(forward)
               25031840  194.416    0.000 1522.239    0.000 level.py:41(notUsed)
               77396496   97.745    0.000 1520.297    0.000 functional.py:1292(leaky_relu)
               77396496 1413.453    0.000 1413.453    0.000 {built-in method torch._C._nn.leaky_relu}
               12897681 1329.241    0.000 1329.241    0.000 {built-in method torch._C._nn.one_hot}
             4749436799  828.319    0.000 1203.992    0.000 enum.py:646(__hash__)
               18401321 1201.931    0.000 1201.931    0.000 {built-in method tensor}
              460205142  132.973    0.000 1152.411    0.000 {built-in method builtins.all}
               30108842  159.462    0.000 1146.467    0.000 tensor.py:21(wrapped)
              705343546  365.811    0.000 1083.372    0.000 overrides.py:1070(has_torch_function)
               62579600  136.220    0.000 1066.927    0.000 layer.py:69(restart)
               77417316 1056.402    0.000 1056.402    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1317222768  305.906    0.000 1051.242    0.000 layers.py:690(<genexpr>)
                4300962  608.270    0.000 1019.973    0.000 collector.py:46(collect)
              245833895 1004.873    0.000 1004.873    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              430096200  635.880    0.000  949.580    0.000 layers.py:62(check)
               77417316  948.938    0.000  948.938    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               77417316  868.665    0.000  868.665    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8601924    9.587    0.000  867.798    0.000 game.py:37(board)
             1705439953  593.949    0.000  800.797    0.000 layer.py:130(add)
               77417316  775.329    0.000  775.329    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             2505482280  626.463    0.000  772.751    0.000 layers.py:700(<genexpr>)
                8596719  269.490    0.000  759.095    0.000 exploration.py:53(softmaxer)
              830262496  373.970    0.000  728.565    0.000 layer.py:126(remove)
              430096300  474.919    0.000  711.811    0.000 layers.py:113(isDone)
               16816882  223.967    0.000  622.229    0.000 random.py:315(sample)
             3438878660  611.957    0.000  611.957    0.000 layer.py:146(elements)
               77417316  609.155    0.000  609.155    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12516020  302.410    0.000  604.182    0.000 layers.py:36(reset)
               25031840   20.851    0.000  597.930    0.000 level.py:38(elementsIn)
              688375600  560.765    0.000  560.765    0.000 level.py:32(inverse)
             6117727538  536.967    0.000  536.967    0.000 layer.py:91(positions)
                8601924   12.273    0.000  484.650    0.000 loss.py:445(forward)
               21504810  475.767    0.000  475.767    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8601924   44.778    0.000  472.377    0.000 functional.py:2637(mse_loss)
               55896891  456.221    0.000  456.221    0.000 {method 't' of 'torch._C._TensorBase' objects}
              430096200  308.247    0.000  452.554    0.000 layers.py:23(check)
               25805772  411.081    0.000  411.081    0.000 {built-in method sum}
             1496691966  321.733    0.000  399.615    0.000 overrides.py:1083(<genexpr>)
             4749468158  375.678    0.000  375.678    0.000 {built-in method builtins.hash}
        3015581579/3015581577  252.517    0.000  374.800    0.000 {built-in method builtins.len}
               25031840  177.814    0.000  361.597    0.000 level.py:39(<listcomp>)
              430096200  153.116    0.000  350.455    0.000 layers.py:104(<listcomp>)
             5250201471  346.035    0.000  346.035    0.000 {method 'append' of 'list' objects}
               12515920  151.680    0.000  343.286    0.000 level.py:16(<dictcomp>)
              527999233  206.509    0.000  298.949    0.000 random.py:250(_randbelow_with_getrandbits)
                8601924  298.631    0.000  298.631    0.000 {built-in method torch._C._nn.mse_loss}
              830262496  292.081    0.000  292.081    0.000 {method 'remove' of 'list' objects}
               42999210   28.623    0.000  290.778    0.000 flatten.py:39(forward)
                4302680  282.332    0.000  282.332    0.000 {method 'ne' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550918: <Rocks_teleport_1> in cluster <dcc> Done

Job <Rocks_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:51 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 19:19:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 19:19:20 2021
Terminated at Mon Apr 26 19:14:40 2021
Results reported at Mon Apr 26 19:14:40 2021

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

    CPU time :                                   85895.95 sec.
    Max Memory :                                 2684 MB
    Average Memory :                             2679.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13700.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            528769 sec.

The output (if any) is above this job summary.

