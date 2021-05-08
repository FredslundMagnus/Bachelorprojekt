
# Parameters

    Name :                      Monsters_simple-0
    Main :                      simple
    Level :                     Levels.MonsterLevel
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      158589862166 function calls (158388096243 primitive calls) in 86102.74 seconds

##    Ordered by: cumulative time
   List reduced from 418 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.735 86102.735 {built-in method builtins.exec}
                      1    0.001    0.001 86102.735 86102.735 <string>:1(<module>)
                      1  129.280  129.280 86102.735 86102.735 main.py:67(simple)
                8406898   32.306    0.000 53003.674    0.006 game.py:42(step)
                8406898   37.484    0.000 51196.977    0.006 layers.py:827(step)
                8406898  683.936    0.000 26839.824    0.003 layers.py:17(step)
                8406898   26.456    0.000 26353.714    0.003 agent.py:29(learn)
                8406898  182.611    0.000 26310.745    0.003 agent.py:117(_learn)
                8406898  661.543    0.000 26128.134    0.003 learner.py:42(Qlearn)
              840689800 2238.027    0.000 26076.301    0.000 layer.py:106(move)
                8406899 1140.684    0.000 24272.941    0.003 layers.py:793(update)
              840689800 2549.970    0.000 18240.308    0.000 layers.py:844(check)
                8406898   48.262    0.000 11427.573    0.001 grad_mode.py:23(decorate_context)
                8406898  279.571    0.000 11287.867    0.001 adam.py:55(step)
              840689800 5484.825    0.000 10261.200    0.000 layers.py:538(check)
               18103270  134.061    0.000 9787.054    0.001 layers.py:849(restart)
                8406898 2050.707    0.000 9722.338    0.001 functional.py:53(adam)
        226986246/25220694  863.489    0.000 9473.504    0.000 module.py:715(_call_impl)
               16813796   40.685    0.000 8812.223    0.001 network.py:28(forward)
               16813796  219.274    0.000 8673.876    0.001 container.py:115(forward)
               18103270   66.541    0.000 8405.327    0.000 level.py:8(__init__)
               18103270 1251.561    0.000 7695.166    0.000 levels.py:428(generate)
             1621335995  876.950    0.000 6241.110    0.000 {built-in method builtins.any}
                8406898   47.163    0.000 5747.089    0.001 tensor.py:181(backward)
                8406898   26.761    0.000 5699.927    0.001 __init__.py:68(backward)
                8406898 5463.690    0.001 5463.690    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               90516350  801.884    0.000 5207.648    0.000 level.py:41(notUsed)
             5809111642 1510.643    0.000 4981.242    0.000 layers.py:809(<genexpr>)
                8406898   97.213    0.000 4898.103    0.001 agent.py:112(__call__)
               50441394 3372.286    0.000 4894.089    0.000 layer.py:159(update)
              840689800  943.708    0.000 4046.926    0.000 layers.py:838(isFree)
            16829634910 2760.368    0.000 3968.059    0.000 enum.py:646(__hash__)
              831087502 2018.922    0.000 3171.753    0.000 layers.py:575(isDead)
             4370486020 2458.257    0.000 3103.218    0.000 layer.py:103(isFree)
               33627592   57.980    0.000 3035.681    0.000 conv.py:422(forward)
               33627592   63.891    0.000 2956.237    0.000 conv.py:414(_conv_forward)
               50441388  114.947    0.000 2949.451    0.000 linear.py:92(forward)
               33627592 2880.196    0.000 2880.196    0.000 {built-in method conv2d}
               50441388  180.972    0.000 2782.660    0.000 functional.py:1669(linear)
              840689800 1931.779    0.000 2717.643    0.000 layers.py:77(check)
              840689900  320.987    0.000 2539.475    0.000 {built-in method builtins.all}
              588482890 1572.235    0.000 2432.296    0.000 tensor.py:933(grad)
               90516350   67.806    0.000 2416.810    0.000 level.py:38(elementsIn)
               35646530 2398.705    0.000 2398.705    0.000 {built-in method tensor}
                8406898  220.932    0.000 2358.073    0.000 optimizer.py:167(zero_grad)
             3420819342  857.956    0.000 2319.704    0.000 layers.py:799(<genexpr>)
              168137960 2040.255    0.000 2040.255    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50441388 1993.835    0.000 1993.835    0.000 {built-in method addmm}
             1223019438  370.208    0.000 1916.290    0.000 random.py:244(randint)
               16813796   16.341    0.000 1781.224    0.000 game.py:38(board)
              168137960 1749.670    0.000 1749.670    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            18115810650 1691.210    0.000 1691.210    0.000 layer.py:99(positions)
             1223019438  647.031    0.000 1546.082    0.000 random.py:200(randrange)
               90516350  757.322    0.000 1533.925    0.000 level.py:39(<listcomp>)
             2776250869 1048.821    0.000 1400.906    0.000 layer.py:138(add)
              840689900  890.919    0.000 1315.586    0.000 layers.py:113(isDone)
             1958151542  849.318    0.000 1310.819    0.000 layer.py:134(remove)
               67255184   52.248    0.000 1293.539    0.000 activation.py:713(forward)
             3861764508 1268.340    0.000 1268.340    0.000 level.py:32(inverse)
              840689800  840.600    0.000 1259.443    0.000 layers.py:48(check)
               67255184   83.925    0.000 1241.290    0.000 functional.py:1292(leaky_relu)
              840689800  434.419    0.000 1235.403    0.000 layers.py:572(<listcomp>)
              108619620  116.638    0.000 1212.963    0.000 layer.py:77(restart)
            16829668619 1207.697    0.000 1207.697    0.000 {built-in method builtins.hash}
             1626748260  821.295    0.000 1174.510    0.000 random.py:250(_randbelow_with_getrandbits)
               67255184 1149.376    0.000 1149.376    0.000 {built-in method torch._C._nn.leaky_relu}
               84068980 1092.926    0.000 1092.926    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              722993308  361.737    0.000 1053.674    0.000 overrides.py:1070(has_torch_function)
             5606019713 1024.471    0.000 1024.471    0.000 layer.py:154(elements)
              840689800  398.379    0.000 1007.856    0.000 layers.py:573(<listcomp>)
               84068980  997.391    0.000  997.391    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               84068980  932.080    0.000  932.080    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              840689800  612.468    0.000  905.753    0.000 layers.py:23(check)
                8406898  528.224    0.000  885.940    0.000 collector.py:46(collect)
               18103370  430.470    0.000  860.686    0.000 layers.py:36(reset)
               84068980  833.421    0.000  833.421    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               90516350  503.694    0.000  815.079    0.000 {built-in method _functools.reduce}
             4670645701  794.384    0.000  794.384    0.000 enum.py:352(<genexpr>)
               90516350  305.520    0.000  773.203    0.000 random.py:315(sample)
               84068980  663.463    0.000  663.463    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18103270  292.699    0.000  607.025    0.000 level.py:16(<dictcomp>)
             8227210601  574.280    0.000  574.280    0.000 {method 'append' of 'list' objects}
        6716445325/6716445324  430.781    0.000  485.299    0.000 {built-in method builtins.len}
             5893235498  473.710    0.000  473.710    0.000 {method 'random' of '_random.Random' objects}
                8406898   12.232    0.000  458.314    0.000 loss.py:445(forward)
                8406898   42.786    0.000  446.082    0.000 functional.py:2637(mse_loss)
             4370486020  432.811    0.000  432.811    0.000 layer.py:211(isBlocking)
               50441388  393.667    0.000  393.667    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8406898   31.261    0.000  379.788    0.000 exploration.py:47(epsilonGreedy)
             1496428004  303.744    0.000  378.991    0.000 overrides.py:1083(<genexpr>)
             3801686700  311.385    0.000  311.385    0.000 level.py:39(<lambda>)
             1958151542  302.161    0.000  302.161    0.000 {method 'remove' of 'list' objects}
             4146936638  298.846    0.000  298.846    0.000 layer.py:92(isDead)
               16813796  284.495    0.000  284.495    0.000 {built-in method sum}
                8406898  280.678    0.000  280.678    0.000 {built-in method torch._C._nn.mse_loss}
                8406898  265.897    0.000  265.897    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8407738  247.532    0.000  247.532    0.000 {built-in method max}
               33627592   25.483    0.000  224.532    0.000 flatten.py:39(forward)
               84069030   98.459    0.000  218.391    0.000 tensor.py:596(__hash__)
             2599726253  213.992    0.000  213.992    0.000 {method 'getrandbits' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578861: <Monsters_simple_0> in cluster <dcc> Done

Job <Monsters_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:08 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu May  6 20:49:59 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 20:49:59 2021
Terminated at Fri May  7 20:45:04 2021
Results reported at Fri May  7 20:45:04 2021

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

    CPU time :                                   85896.50 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2063.42 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86107 sec.
    Turnaround time :                            950456 sec.

The output (if any) is above this job summary.

