Start
True
True
['main.py', '-name', 'Diamonds4_simple-0', '-hours', '24.0', '-level', 'Levels.Causal7', '-main', 'simple', '-network2', 'Networks.MiniBig']

# Parameters

    Name :                      Diamonds4_simple-0
    Main :                      simple
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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


      162668061001 function calls (162377536662 primitive calls) in 86115.43 seconds

##    Ordered by: cumulative time
   List reduced from 410 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.427 86115.427 {built-in method builtins.exec}
                      1    0.001    0.001 86115.427 86115.427 <string>:1(<module>)
                      1  181.935  181.935 86115.426 86115.426 main.py:71(simple)
               12105166   39.462    0.000 46953.863    0.004 game.py:41(step)
               12105166   53.680    0.000 44476.489    0.004 layers.py:718(step)
               12105166   35.650    0.000 30483.798    0.003 agent.py:29(learn)
               12105166  267.364    0.000 30421.821    0.003 agent.py:117(_learn)
               12105166  781.427    0.000 30154.457    0.002 learner.py:42(Qlearn)
               12105167 1660.909    0.000 26173.383    0.002 layers.py:684(update)
               12105166  892.899    0.000 18177.669    0.002 layers.py:17(step)
             1210516600 1743.042    0.000 17177.503    0.000 layer.py:98(move)
               35653696  263.722    0.000 13228.916    0.000 layers.py:740(restart)
               12105166   71.634    0.000 12334.699    0.001 grad_mode.py:23(decorate_context)
               12105166  404.211    0.000 12130.693    0.001 adam.py:55(step)
        326839482/36315498 1198.119    0.000 11935.914    0.000 module.py:715(_call_impl)
               24210332   50.406    0.000 11051.780    0.000 network.py:27(forward)
               24210332  283.393    0.000 10858.270    0.000 container.py:115(forward)
               35653696  123.715    0.000 10580.132    0.000 level.py:8(__init__)
               12105166 2204.714    0.000 9938.093    0.001 functional.py:53(adam)
             1210516600 2517.416    0.000 9721.918    0.000 layers.py:735(check)
               35653696  385.509    0.000 9316.342    0.000 levels.py:441(generate)
              171130892 1536.543    0.000 8529.776    0.000 level.py:41(notUsed)
               12105166   68.226    0.000 6791.576    0.001 tensor.py:181(backward)
               12105166   40.558    0.000 6723.350    0.001 __init__.py:68(backward)
               12105166 6411.971    0.001 6411.971    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12105166  138.881    0.000 6182.286    0.001 agent.py:112(__call__)
               84736169 2799.311    0.000 5040.780    0.000 layer.py:167(NoRock_update)
             2312748689 1355.107    0.000 4873.343    0.000 {built-in method builtins.any}
             1210516600 1181.903    0.000 4569.439    0.000 layers.py:729(isFree)
            16389331259 2790.294    0.000 4132.930    0.000 enum.py:646(__hash__)
              171130892  118.786    0.000 4019.987    0.000 level.py:38(elementsIn)
               48420664   82.838    0.000 3851.953    0.000 conv.py:422(forward)
               48420664   97.641    0.000 3737.219    0.000 conv.py:414(_conv_forward)
               72630996  169.050    0.000 3679.479    0.000 linear.py:92(forward)
               48420664 3622.926    0.000 3622.926    0.000 {built-in method conv2d}
               72630996  269.608    0.000 3429.538    0.000 functional.py:1669(linear)
               51184137 3418.978    0.000 3418.978    0.000 {built-in method tensor}
             5299593132 2721.344    0.000 3387.536    0.000 layer.py:95(isFree)
              847361650 1918.935    0.000 3219.108    0.000 tensor.py:933(grad)
             9398904032 2383.831    0.000 2926.967    0.000 layers.py:700(<genexpr>)
               12105166  263.686    0.000 2782.311    0.000 optimizer.py:167(zero_grad)
               24210332   22.222    0.000 2667.493    0.000 game.py:37(board)
              171130892 1277.458    0.000 2616.465    0.000 level.py:39(<listcomp>)
               72630996 2404.139    0.000 2404.139    0.000 {built-in method addmm}
              249575872  182.160    0.000 2297.670    0.000 layer.py:69(restart)
              242103320 2001.328    0.000 2001.328    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1210516700  303.075    0.000 1899.284    0.000 {built-in method builtins.all}
               35653796  916.446    0.000 1832.852    0.000 layers.py:36(reset)
             8216430323 1756.410    0.000 1756.410    0.000 level.py:32(inverse)
             3233928084  787.392    0.000 1746.234    0.000 layers.py:690(<genexpr>)
              242103320 1697.343    0.000 1697.343    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              605278370 1033.529    0.000 1695.472    0.000 layers.py:617(check)
              605251278 1031.982    0.000 1669.343    0.000 layers.py:602(check)
              605282905 1016.297    0.000 1653.606    0.000 layers.py:632(check)
             1041044356  527.626    0.000 1588.106    0.000 overrides.py:1070(has_torch_function)
               96841328   82.707    0.000 1526.845    0.000 activation.py:713(forward)
               96841328  130.714    0.000 1444.138    0.000 functional.py:1292(leaky_relu)
            16389379768 1342.646    0.000 1342.646    0.000 {built-in method builtins.hash}
             7444246663 1333.776    0.000 1333.776    0.000 enum.py:352(<genexpr>)
               96841328 1300.604    0.000 1300.604    0.000 {built-in method torch._C._nn.leaky_relu}
              171130892  803.234    0.000 1284.737    0.000 {built-in method _functools.reduce}
             3621960665 1274.364    0.000 1274.364    0.000 layer.py:146(elements)
            12937597397 1204.696    0.000 1204.696    0.000 layer.py:91(positions)
              121051660 1138.721    0.000 1138.721    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              121051660 1069.661    0.000 1069.661    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               35653696  490.192    0.000 1055.181    0.000 level.py:16(<dictcomp>)
               12105166  595.457    0.000 1023.675    0.000 collector.py:46(collect)
              121051660  951.916    0.000  951.916    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1729063197  658.505    0.000  903.528    0.000 layer.py:130(add)
              121051660  838.921    0.000  838.921    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              605275470  535.740    0.000  811.054    0.000 layers.py:588(check)
        10729371158/10729371157  690.423    0.000  764.232    0.000 {built-in method builtins.len}
             9838958842  734.648    0.000  734.648    0.000 {method 'random' of '_random.Random' objects}
              605264517  446.183    0.000  653.573    0.000 layers.py:23(check)
              121051660  634.378    0.000  634.378    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12105166   16.030    0.000  595.033    0.000 loss.py:445(forward)
             2154719708  466.488    0.000  583.680    0.000 overrides.py:1083(<genexpr>)
               12105166   66.806    0.000  579.003    0.000 functional.py:2637(mse_loss)
             8224041028  543.137    0.000  543.137    0.000 layer.py:84(isDead)
             5299593132  525.557    0.000  525.557    0.000 layer.py:203(isBlocking)
               12105166   41.489    0.000  504.840    0.000 exploration.py:47(epsilonGreedy)
             5989581220  481.503    0.000  481.503    0.000 level.py:39(<lambda>)
             1210516700  341.465    0.000  463.425    0.000 layers.py:592(isDone)
               72630996  441.083    0.000  441.083    0.000 {method 't' of 'torch._C._TensorBase' objects}
               12105166  363.219    0.000  363.219    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
             4668644566  357.507    0.000  357.507    0.000 {method 'append' of 'list' objects}
             2923611846  354.232    0.000  354.232    0.000 layer.py:182(grid)
               12105166  335.260    0.000  335.260    0.000 {built-in method torch._C._nn.mse_loss}
               24210332  330.083    0.000  330.083    0.000 {built-in method sum}
              121051710  142.305    0.000  325.437    0.000 tensor.py:596(__hash__)
              175276448  202.302    0.000  311.352    0.000 layers.py:113(isDone)
              421914638  203.673    0.000  304.449    0.000 layer.py:126(remove)
               12106376  303.915    0.000  303.915    0.000 {built-in method max}
               84736169  275.755    0.000  275.755    0.000 layer.py:178(<listcomp>)
              171130892   94.648    0.000  261.048    0.000 random.py:285(choice)
               12105166   50.341    0.000  260.134    0.000 __init__.py:28(_make_grads)
               84736169  253.806    0.000  253.806    0.000 layer.py:179(<listcomp>)
               12105166  253.496    0.000  253.496    0.000 {built-in method gather}
               48420664   32.094    0.000  251.570    0.000 flatten.py:39(forward)
               12105166   56.569    0.000  236.276    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578843: <Diamonds4_simple_0> in cluster <dcc> Done

Job <Diamonds4_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun May  2 02:23:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 02:23:20 2021
Terminated at Mon May  3 02:18:42 2021
Results reported at Mon May  3 02:18:42 2021

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

    CPU time :                                   85896.30 sec.
    Max Memory :                                 2068 MB
    Average Memory :                             2065.57 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14316.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            538477 sec.

The output (if any) is above this job summary.

