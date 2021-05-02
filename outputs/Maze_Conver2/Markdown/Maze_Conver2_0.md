
# Parameters

    Name :                      Maze_Conver2-0
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60086852903 function calls (59763733672 primitive calls) in 86070.20 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.404 86110.404 {built-in method builtins.exec}
                      1    5.521    5.521 86110.404 86110.404 <string>:1(<module>)
                      1  461.864  461.864 86104.883 86104.883 main.py:79(CFagent)
               10676235   51.431    0.000 27646.705    0.003 agent.py:29(learn)
               10676229  705.675    0.000 22338.127    0.002 learner.py:42(Qlearn)
                3558745   21.137    0.000 17913.869    0.005 game.py:41(step)
                3558745   24.411    0.000 17090.847    0.005 layers.py:718(step)
        361906479/38788939 1561.085    0.000 12406.148    0.000 module.py:866(_call_impl)
               28112710   82.008    0.000 11524.043    0.000 network.py:27(forward)
               28112710  380.953    0.000 11244.775    0.000 container.py:117(forward)
                3558745  427.710    0.000 10772.967    0.003 agent.py:54(_learn)
                3558745  421.702    0.000 9799.720    0.003 agent.py:204(_learn)
                3558745  359.864    0.000 9795.287    0.003 layers.py:17(step)
              355679243  606.640    0.000 9401.698    0.000 layer.py:98(move)
                3558745 7906.691    0.002 9118.421    0.003 replaybuffer.py:22(sample_data)
                3558745 7750.918    0.002 8904.173    0.003 replaybuffer.py:67(sample_data)
               10676229  114.321    0.000 8651.981    0.001 optimizer.py:84(wrapper)
                3558745  686.366    0.000 8587.416    0.002 agent.py:212(counterfact)
               10676229   58.121    0.000 8190.785    0.001 grad_mode.py:24(decorate_context)
               10676229  363.758    0.000 8013.423    0.001 adam.py:55(step)
               10676229 1653.217    0.000 7273.035    0.001 _functional.py:53(adam)
                3558746  531.780    0.000 7231.774    0.002 layers.py:684(update)
                3558745  117.808    0.000 6997.364    0.002 agent.py:117(_learn)
                8703670  270.488    0.000 6002.032    0.001 agent.py:49(__call__)
               10676229   46.953    0.000 5879.669    0.001 tensor.py:195(backward)
               10676229   50.503    0.000 5831.054    0.001 __init__.py:68(backward)
               10676229 5549.228    0.001 5549.228    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              355679243 1253.142    0.000 5201.570    0.000 layers.py:735(check)
               48001724 4350.984    0.000 4350.984    0.000 {built-in method tensor}
               56225420  129.255    0.000 4188.395    0.000 conv.py:398(forward)
               56939928 2339.697    0.000 4172.216    0.000 layer.py:167(NoRock_update)
               39831637   27.334    0.000 4131.889    0.000 game.py:37(board)
               56225420   90.465    0.000 3994.974    0.000 conv.py:390(_conv_forward)
                3558745 1543.791    0.000 3923.275    0.001 agent.py:88(interveen)
               56225420 3904.509    0.000 3904.509    0.000 {built-in method conv2d}
               77220640  161.143    0.000 3178.908    0.000 linear.py:93(forward)
              355679243  543.599    0.000 3079.367    0.000 layers.py:729(isFree)
                3558745 1685.945    0.000 2935.242    0.001 replaybuffer.py:28(teleporter_save_data)
               77220640   63.650    0.000 2930.441    0.000 functional.py:1737(linear)
               77220640 2851.173    0.000 2851.173    0.000 {built-in method torch._C._nn.linear}
                3558745 1809.726    0.001 2769.540    0.001 agent.py:67(modify)
             2232177314 2188.481    0.000 2535.768    0.000 layer.py:95(isFree)
                1615327   35.009    0.000 2272.205    0.001 agent.py:176(choose_action)
                2628862   44.680    0.000 2105.108    0.001 layers.py:740(restart)
               47849835 1937.545    0.000 1937.545    0.000 {built-in method cat}
                2628862   25.623    0.000 1809.510    0.001 level.py:8(__init__)
               12262415   90.058    0.000 1716.817    0.000 agent.py:59(modify_board)
                3558739   75.818    0.000 1701.507    0.000 agent.py:172(__call__)
              105333350   91.062    0.000 1646.358    0.000 activation.py:713(forward)
                3583865  232.775    0.000 1613.118    0.000 levels.py:9(generate)
                3558745   74.088    0.000 1581.603    0.000 agent.py:112(__call__)
              105333350   85.734    0.000 1555.296    0.000 functional.py:1364(leaky_relu)
              355679243  942.937    0.000 1528.020    0.000 layers.py:168(check)
              105333350 1452.458    0.000 1452.458    0.000 {built-in method torch._C._nn.leaky_relu}
              199289600 1423.482    0.000 1423.482    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              356804484  313.871    0.000 1369.249    0.000 {built-in method builtins.any}
              199289600 1264.360    0.000 1264.360    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              117088050 1258.060    0.000 1258.060    0.000 {built-in method clone}
               10676229  221.993    0.000 1249.334    0.000 optimizer.py:189(zero_grad)
                3558745  918.082    0.000 1135.901    0.000 replaybuffer.py:73(CF_save_data)
               12262415 1123.241    0.000 1123.241    0.000 {built-in method torch._C._nn.one_hot}
             1147277149 1120.462    0.000 1120.462    0.000 layer.py:146(elements)
             3179211642  881.837    0.000 1055.378    0.000 layers.py:700(<genexpr>)
             3566397059  678.982    0.000  966.435    0.000 enum.py:646(__hash__)
              355874600  168.965    0.000  945.480    0.000 {built-in method builtins.all}
                3558745   72.515    0.000  914.975    0.000 replaybuffer.py:18(stacker)
                3558739   69.153    0.000  868.679    0.000 replaybuffer.py:63(stacker)
               99644800  827.993    0.000  827.993    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1862446578  508.664    0.000  820.325    0.000 layers.py:690(<genexpr>)
               99644800  724.125    0.000  724.125    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               99644800  678.593    0.000  678.593    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               99644800  672.805    0.000  672.805    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              355679243  423.798    0.000  653.365    0.000 layers.py:141(check)
               16914082  257.689    0.000  644.794    0.000 random.py:315(sample)
                8703670  223.453    0.000  624.309    0.000 exploration.py:53(softmaxer)
        7869868427/7869868424  545.812    0.000  616.274    0.000 {built-in method builtins.len}
              355679243  413.692    0.000  583.111    0.000 layers.py:48(check)
              697513684  465.439    0.000  576.630    0.000 tensor.py:906(grad)
                3558745  327.943    0.000  557.905    0.000 collector.py:46(collect)
                7886586   68.222    0.000  553.405    0.000 level.py:41(notUsed)
             5609649236  533.747    0.000  533.747    0.000 layer.py:91(positions)
               10676229   21.904    0.000  524.905    0.000 loss.py:527(forward)
               99644800  503.126    0.000  503.126    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10676229   54.151    0.000  503.001    0.000 functional.py:2898(mse_loss)
                3583865  265.370    0.000  492.961    0.000 levels.py:75(RFS)
              355679243  326.623    0.000  489.390    0.000 layers.py:124(check)
                1615327  358.382    0.000  409.223    0.000 agent.py:187(convert_values)
              355679243  257.448    0.000  380.639    0.000 layers.py:23(check)
              517227947  231.843    0.000  330.406    0.000 layer.py:130(add)
              365672401  222.530    0.000  321.651    0.000 layer.py:126(remove)
                7117492  305.816    0.000  305.816    0.000 {built-in method nonzero}
              443455132  204.413    0.000  302.934    0.000 random.py:250(_randbelow_with_getrandbits)
               10676229  300.406    0.000  300.406    0.000 {built-in method torch._C._nn.mse_loss}
              132909204  290.287    0.000  290.287    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3566437522  287.460    0.000  287.460    0.000 {built-in method builtins.hash}
               10677454  275.528    0.000  275.528    0.000 {built-in method max}
               56225420   44.178    0.000  273.813    0.000 flatten.py:39(forward)
             3204867189  252.927    0.000  252.927    0.000 {method 'random' of '_random.Random' objects}
               56939928  249.900    0.000  249.900    0.000 layer.py:178(<listcomp>)
               21030896   34.274    0.000  243.501    0.000 layer.py:69(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579175: <Maze_Conver2_0> in cluster <dcc> Done

Job <Maze_Conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 30 15:35:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 15:35:18 2021
Terminated at Sat May  1 15:30:33 2021
Results reported at Sat May  1 15:30:33 2021

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

    CPU time :                                   85889.58 sec.
    Max Memory :                                 9900 MB
    Average Memory :                             6491.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6484.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            391585 sec.

The output (if any) is above this job summary.

