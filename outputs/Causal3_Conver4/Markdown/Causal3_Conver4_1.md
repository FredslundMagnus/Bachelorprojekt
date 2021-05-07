
# Parameters

    Name :                      Causal3_Conver4-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55008301737 function calls (54716935014 primitive calls) in 86125.59 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86125.594 86125.594 {built-in method builtins.exec}
                      1    4.450    4.450 86125.594 86125.594 <string>:1(<module>)
                      1  348.248  348.248 86121.143 86121.143 main.py:80(CFagent)
                9145653   35.415    0.000 30188.957    0.003 agent.py:29(learn)
                9145653  751.064    0.000 25207.289    0.003 learner.py:42(Qlearn)
                3048551   14.380    0.000 15884.738    0.005 game.py:42(step)
                3048551   20.597    0.000 15155.366    0.005 layers.py:827(step)
        325807288/34442256 1465.519    0.000 13256.187    0.000 module.py:866(_call_impl)
               25296603   73.897    0.000 12452.556    0.000 network.py:28(forward)
               25296603  391.399    0.000 12198.429    0.000 container.py:117(forward)
                3048551  335.617    0.000 11635.085    0.004 agent.py:54(_learn)
                3048551  330.360    0.000 10794.442    0.004 agent.py:204(_learn)
                9145653   87.474    0.000 10700.579    0.001 optimizer.py:84(wrapper)
                9145653   40.592    0.000 10295.951    0.001 grad_mode.py:24(decorate_context)
                9145653  294.734    0.000 10161.115    0.001 adam.py:55(step)
                3048551  276.566    0.000 9564.060    0.003 layers.py:17(step)
                9145653 2095.869    0.000 9522.339    0.001 _functional.py:53(adam)
                3048551 1036.465    0.000 9353.281    0.003 agent.py:212(counterfact)
              304635027  544.815    0.000 9255.284    0.000 layer.py:106(move)
                3048551   97.827    0.000 7701.635    0.003 agent.py:117(_learn)
                3048551 3606.871    0.001 6738.444    0.002 replaybuffer.py:28(teleporter_save_data)
                8074299  228.609    0.000 6408.699    0.001 agent.py:49(__call__)
                9145653   39.187    0.000 6246.815    0.001 tensor.py:195(backward)
                9145653   37.593    0.000 6206.139    0.001 __init__.py:68(backward)
                9145653 5945.136    0.001 5945.136    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3048551 3358.707    0.001 5775.176    0.002 agent.py:88(interveen)
                3048552  473.212    0.000 5545.433    0.002 layers.py:793(update)
              304635027 1194.624    0.000 5496.615    0.000 layers.py:844(check)
                3048551 4245.160    0.001 5306.278    0.002 replaybuffer.py:22(sample_data)
                3048551 4060.686    0.001 5093.354    0.002 replaybuffer.py:67(sample_data)
               50593206  118.046    0.000 4360.228    0.000 conv.py:398(forward)
               50593206   72.264    0.000 4188.366    0.000 conv.py:390(_conv_forward)
               50593206 4116.103    0.000 4116.103    0.000 {built-in method conv2d}
               43512523 4012.014    0.000 4012.014    0.000 {built-in method tensor}
               36467596   27.745    0.000 3792.170    0.000 game.py:38(board)
               69792707  155.718    0.000 3527.583    0.000 linear.py:93(forward)
                1979549   47.798    0.000 3423.162    0.002 agent.py:176(choose_action)
               69792707   60.029    0.000 3297.625    0.000 functional.py:1737(linear)
               69792707 3220.894    0.000 3220.894    0.000 {built-in method torch._C._nn.linear}
               48776824 1762.438    0.000 3141.805    0.000 layer.py:175(NoRock_update)
                3048551 1980.653    0.001 2951.225    0.001 agent.py:67(modify)
              203431207 2869.245    0.000 2869.245    0.000 {built-in method clone}
              304635027  554.879    0.000 2711.281    0.000 layers.py:838(isFree)
             2278333352 1785.066    0.000 2156.401    0.000 layer.py:103(isFree)
               95089310  100.870    0.000 2010.666    0.000 activation.py:713(forward)
              170718856 1946.963    0.000 1946.963    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               95089310   88.434    0.000 1909.796    0.000 functional.py:1364(leaky_relu)
               41608360 1835.269    0.000 1835.269    0.000 {built-in method cat}
               95089310 1802.470    0.000 1802.470    0.000 {built-in method torch._C._nn.leaky_relu}
               11122850   85.418    0.000 1757.639    0.000 agent.py:59(modify_board)
              170718856 1720.225    0.000 1720.225    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3048551   57.019    0.000 1691.972    0.001 agent.py:172(__call__)
                3048551 1268.710    0.000 1676.331    0.001 replaybuffer.py:73(CF_save_data)
                3048551   54.540    0.000 1584.783    0.001 agent.py:112(__call__)
                9145653  237.340    0.000 1497.952    0.000 optimizer.py:189(zero_grad)
                4002538   47.054    0.000 1438.413    0.000 layers.py:849(restart)
             4602998295  868.290    0.000 1276.823    0.000 enum.py:646(__hash__)
              303901214  282.285    0.000 1212.927    0.000 {built-in method builtins.any}
              304635027  729.674    0.000 1157.489    0.000 layers.py:246(check)
               11122850 1116.147    0.000 1116.147    0.000 {built-in method torch._C._nn.one_hot}
              304635027  621.657    0.000 1055.716    0.000 layers.py:286(check)
               85359428 1054.167    0.000 1054.167    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4002538   22.269    0.000 1037.620    0.000 level.py:8(__init__)
             2707673958  771.507    0.000  930.642    0.000 layers.py:809(<genexpr>)
               85359428  925.443    0.000  925.443    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               85359428  883.553    0.000  883.553    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85359428  868.638    0.000  868.638    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3048551   61.337    0.000  825.676    0.000 replaybuffer.py:18(stacker)
                4002538   88.413    0.000  814.000    0.000 levels.py:164(generate)
                3048551   64.814    0.000  805.647    0.000 replaybuffer.py:63(stacker)
             1079314979  774.495    0.000  774.495    0.000 layer.py:154(elements)
              217602608  763.534    0.000  763.534    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1979549  615.229    0.000  723.372    0.000 agent.py:187(convert_values)
                3048551  422.740    0.000  700.211    0.000 collector.py:46(collect)
               85359428  683.430    0.000  683.430    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8074299  243.762    0.000  663.663    0.000 exploration.py:53(softmaxer)
              304855200   76.079    0.000  642.696    0.000 {built-in method builtins.all}
                8005076   84.561    0.000  608.182    0.000 level.py:41(notUsed)
              772597863  192.559    0.000  606.622    0.000 layers.py:799(<genexpr>)
        6917813852/6917813849  515.423    0.000  581.711    0.000 {built-in method builtins.len}
              597516080  465.374    0.000  575.250    0.000 tensor.py:906(grad)
             5739934033  563.255    0.000  563.255    0.000 layer.py:99(positions)
               14102178  202.595    0.000  532.864    0.000 random.py:315(sample)
              304635027  331.648    0.000  524.770    0.000 layers.py:313(check)
              304635027  315.353    0.000  505.160    0.000 layers.py:273(check)
                9145653   13.396    0.000  485.897    0.000 loss.py:527(forward)
                9145653   35.948    0.000  472.500    0.000 functional.py:2898(mse_loss)
              304635027  299.920    0.000  450.295    0.000 layers.py:48(check)
             4603033046  408.539    0.000  408.539    0.000 {built-in method builtins.hash}
              304635027  231.266    0.000  347.315    0.000 layers.py:23(check)
               32020304   42.756    0.000  341.906    0.000 layer.py:77(restart)
               50593206   37.490    0.000  325.194    0.000 flatten.py:39(forward)
                9145653  315.231    0.000  315.231    0.000 {built-in method torch._C._nn.mse_loss}
              492616802  228.842    0.000  309.121    0.000 layer.py:138(add)
               18291306  295.069    0.000  295.069    0.000 {built-in method sum}
               50593206  287.704    0.000  287.704    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              407029138  192.799    0.000  281.597    0.000 random.py:250(_randbelow_with_getrandbits)
                6097104  281.468    0.000  281.468    0.000 {built-in method nonzero}
                9146764  279.997    0.000  279.997    0.000 {built-in method max}
              146185989  186.926    0.000  277.464    0.000 layers.py:113(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9615514: <Causal3_Conver4_1> in cluster <dcc> Done

Job <Causal3_Conver4_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May  4 23:51:55 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May  5 06:38:37 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 06:38:37 2021
Terminated at Thu May  6 06:34:13 2021
Results reported at Thu May  6 06:34:13 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85902.56 sec.
    Max Memory :                                 9232 MB
    Average Memory :                             6389.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7152.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86137 sec.
    Turnaround time :                            110538 sec.

The output (if any) is above this job summary.

