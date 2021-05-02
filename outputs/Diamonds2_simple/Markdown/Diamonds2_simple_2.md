
# Parameters

    Name :                      Diamonds2_simple-2
    Main :                      simple
    Level :                     Levels.Causal5
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
    Network2 :                  Networks.MiniBig
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


      193262836395 function calls (193002409544 primitive calls) in 86111.11 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.107 86111.107 {built-in method builtins.exec}
                      1    0.001    0.001 86111.107 86111.107 <string>:1(<module>)
                      1  149.537  149.537 86111.107 86111.107 main.py:66(simple)
               10851104   32.932    0.000 52590.509    0.005 game.py:41(step)
               10851104   47.665    0.000 50269.708    0.005 layers.py:718(step)
               10851104  768.909    0.000 28263.857    0.003 layers.py:17(step)
             1085110400 1630.895    0.000 27405.351    0.000 layer.py:98(move)
               10851104   34.207    0.000 25919.089    0.002 agent.py:29(learn)
               10851104  228.035    0.000 25864.251    0.002 agent.py:117(_learn)
               10851104  663.882    0.000 25636.216    0.002 learner.py:42(Qlearn)
               10851105 1379.547    0.000 21900.961    0.002 layers.py:684(update)
             1085110400 3972.817    0.000 19473.120    0.000 layers.py:735(check)
               10851104   64.155    0.000 10619.840    0.001 grad_mode.py:23(decorate_context)
               10851104  332.302    0.000 10448.285    0.001 adam.py:55(step)
        292979808/32553312 1018.698    0.000 10128.771    0.000 module.py:715(_call_impl)
               21702208   45.960    0.000 9380.559    0.000 network.py:27(forward)
               21702208  240.740    0.000 9213.792    0.000 container.py:115(forward)
               19338877  168.576    0.000 8788.809    0.000 layers.py:740(restart)
               10851104 1945.085    0.000 8627.946    0.001 functional.py:53(adam)
               19338877   77.538    0.000 7317.654    0.000 level.py:8(__init__)
               19338877  271.347    0.000 6609.822    0.000 levels.py:249(generate)
              125703265 1079.841    0.000 6057.888    0.000 level.py:41(notUsed)
               10851104   56.873    0.000 5736.610    0.001 tensor.py:181(backward)
               10851104   35.623    0.000 5679.737    0.001 __init__.py:68(backward)
               10851104 5416.858    0.000 5416.858    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10851104  119.265    0.000 5268.716    0.000 agent.py:112(__call__)
            22421792760 3540.043    0.000 5097.749    0.000 enum.py:646(__hash__)
             1085110400 1415.957    0.000 5032.905    0.000 layers.py:729(isFree)
             2085775480 1308.301    0.000 4958.355    0.000 {built-in method builtins.any}
               97659945 2671.961    0.000 4894.214    0.000 layer.py:167(NoRock_update)
             6899565840 2835.239    0.000 3616.949    0.000 layer.py:95(isFree)
               45915999 3349.356    0.000 3349.356    0.000 {built-in method tensor}
               43404416   66.845    0.000 3327.423    0.000 conv.py:422(forward)
               43404416   85.668    0.000 3233.933    0.000 conv.py:414(_conv_forward)
            10657716230 2572.136    0.000 3161.169    0.000 layers.py:700(<genexpr>)
               43404416 3134.123    0.000 3134.123    0.000 {built-in method conv2d}
               65106624  131.627    0.000 3070.823    0.000 linear.py:92(forward)
               65106624  217.880    0.000 2879.230    0.000 functional.py:1669(linear)
             1085110400 1786.448    0.000 2872.965    0.000 layers.py:375(check)
              125703265   83.058    0.000 2801.106    0.000 level.py:38(elementsIn)
             1085110400 1719.568    0.000 2770.346    0.000 layers.py:349(check)
               21702208   18.715    0.000 2705.850    0.000 game.py:37(board)
             1085110400 1678.469    0.000 2698.248    0.000 layers.py:387(check)
             1085110400 1671.562    0.000 2680.728    0.000 layers.py:337(check)
              759577310 1589.955    0.000 2662.571    0.000 tensor.py:933(grad)
               10851104  210.259    0.000 2312.603    0.000 optimizer.py:167(zero_grad)
             1085110500  414.617    0.000 2311.818    0.000 {built-in method builtins.all}
            24126187622 2151.575    0.000 2151.575    0.000 layer.py:91(positions)
               65106624 2028.265    0.000 2028.265    0.000 {built-in method addmm}
             4885127064 1211.187    0.000 2019.639    0.000 layers.py:690(<genexpr>)
              125703265  900.060    0.000 1818.826    0.000 level.py:39(<listcomp>)
              217022080 1731.465    0.000 1731.465    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
            22421836269 1557.714    0.000 1557.714    0.000 {built-in method builtins.hash}
              217022080 1456.228    0.000 1456.228    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              933195024  441.364    0.000 1313.606    0.000 overrides.py:1070(has_torch_function)
             5928597840 1307.106    0.000 1307.106    0.000 level.py:32(inverse)
               86808832   63.440    0.000 1289.640    0.000 activation.py:713(forward)
             1085110400  823.854    0.000 1270.987    0.000 layers.py:364(check)
              174049893  121.408    0.000 1248.164    0.000 layer.py:69(restart)
             1085110400  812.051    0.000 1244.673    0.000 layers.py:326(check)
               86808832  107.633    0.000 1226.200    0.000 functional.py:1292(leaky_relu)
             3130930937 1211.654    0.000 1211.654    0.000 layer.py:146(elements)
               86808832 1107.991    0.000 1107.991    0.000 {built-in method torch._C._nn.leaky_relu}
             1085110400  730.528    0.000 1075.243    0.000 layers.py:23(check)
              108511040  984.266    0.000  984.266    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               19338977  469.759    0.000  945.085    0.000 layers.py:36(reset)
              108511040  925.819    0.000  925.819    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             5221518679  904.834    0.000  904.834    0.000 enum.py:352(<genexpr>)
              125703265  559.883    0.000  899.221    0.000 {built-in method _functools.reduce}
               10851104  506.619    0.000  877.019    0.000 collector.py:46(collect)
              108511040  832.470    0.000  832.470    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
            10977988366  808.698    0.000  808.698    0.000 {method 'random' of '_random.Random' objects}
        12828972472/12828972471  738.812    0.000  803.598    0.000 {built-in method builtins.len}
             1471357459  551.536    0.000  761.412    0.000 layer.py:130(add)
              108511040  724.045    0.000  724.045    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6899565840  636.750    0.000  636.750    0.000 layer.py:203(isBlocking)
             9591944607  589.032    0.000  589.032    0.000 layer.py:84(isDead)
               19338877  287.661    0.000  577.498    0.000 level.py:16(<dictcomp>)
              108511040  549.016    0.000  549.016    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10851104   15.019    0.000  500.341    0.000 loss.py:445(forward)
              740208237  330.185    0.000  490.343    0.000 layer.py:126(remove)
               10851104   52.117    0.000  485.322    0.000 functional.py:2637(mse_loss)
             1931496672  387.907    0.000  482.592    0.000 overrides.py:1083(<genexpr>)
               10851104   35.833    0.000  423.154    0.000 exploration.py:47(epsilonGreedy)
             1085110500  294.486    0.000  405.817    0.000 layers.py:354(isDone)
               65106624  368.057    0.000  368.057    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4399614275  339.339    0.000  339.339    0.000 level.py:39(<lambda>)
             4362130732  337.584    0.000  337.584    0.000 {method 'append' of 'list' objects}
               10851104  298.475    0.000  298.475    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               21702208  285.449    0.000  285.449    0.000 {built-in method sum}
               97659945  284.609    0.000  284.609    0.000 layer.py:178(<listcomp>)
               10851104  281.960    0.000  281.960    0.000 {built-in method torch._C._nn.mse_loss}
               97659945  280.422    0.000  280.422    0.000 layer.py:179(<listcomp>)
              108511090  116.789    0.000  268.144    0.000 tensor.py:596(__hash__)
               10852189  255.708    0.000  255.708    0.000 {built-in method max}
               43404416   32.006    0.000  220.511    0.000 flatten.py:39(forward)
               10851104   41.182    0.000  218.500    0.000 __init__.py:28(_make_grads)
               10851104  212.565    0.000  212.565    0.000 {built-in method gather}
               10851104   49.263    0.000  200.029    0.000 tensor.py:506(__rsub__)
              292979808  189.125    0.000  189.125    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578839: <Diamonds2_simple_2> in cluster <dcc> Done

Job <Diamonds2_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 30 17:42:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 17:42:18 2021
Terminated at Sat May  1 17:37:37 2021
Results reported at Sat May  1 17:37:37 2021

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

    CPU time :                                   85900.23 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2059.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            420812 sec.

The output (if any) is above this job summary.

