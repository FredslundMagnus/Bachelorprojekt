
# Parameters

    Name :                      9x9_gamme0.95-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      23837929586 function calls (23704866535 primitive calls) in 35691.67 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.587 35709.587 {built-in method builtins.exec}
                      1    0.769    0.769 35709.587 35709.587 <string>:1(<module>)
                      1  116.319  116.319 35708.817 35708.817 main.py:10(teleport)
                4752400   18.028    0.000 13727.132    0.003 agent.py:26(learn)
                4752400  365.864    0.000 11736.324    0.002 learner.py:42(Qlearn)
                2376200   94.045    0.000 8189.734    0.003 agent.py:50(_learn)
                2376200   10.174    0.000 7353.895    0.003 game.py:21(step)
                2376200   11.267    0.000 6810.426    0.003 layers.py:212(step)
        149695010/16632970  619.139    0.000 5671.404    0.000 module.py:866(_call_impl)
                2376200   80.190    0.000 5508.713    0.002 agent.py:101(_learn)
               11880570   35.765    0.000 5287.619    0.000 network.py:24(forward)
               11880570  167.716    0.000 5177.838    0.000 container.py:117(forward)
                2376200 2821.202    0.001 5042.561    0.002 replaybuffer.py:27(teleporter_save_data)
                4752400   42.696    0.000 4908.057    0.001 optimizer.py:84(wrapper)
                4752400   20.655    0.000 4707.601    0.001 grad_mode.py:24(decorate_context)
                4752400  136.133    0.000 4639.990    0.001 adam.py:55(step)
                2376200  162.239    0.000 4400.152    0.002 layers.py:17(step)
                4752400  968.589    0.000 4347.287    0.001 _functional.py:53(adam)
              237620000  220.482    0.000 4217.586    0.000 layer.py:66(move)
                2376200 2410.561    0.001 4137.811    0.002 agent.py:77(interveen)
                4751970  125.284    0.000 3501.183    0.001 agent.py:45(__call__)
                4752400   22.438    0.000 2901.267    0.001 tensor.py:195(backward)
                4752400   19.255    0.000 2878.096    0.001 __init__.py:68(backward)
                4752400 2752.835    0.001 2752.835    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              237620000  482.884    0.000 2420.459    0.000 layers.py:229(check)
                2376201  207.557    0.000 2382.624    0.001 layers.py:192(update)
               23761140   53.210    0.000 1895.326    0.000 conv.py:398(forward)
               23761140   31.885    0.000 1819.727    0.000 conv.py:390(_conv_forward)
              146906230 1806.800    0.000 1806.800    0.000 {built-in method clone}
               23761140 1787.842    0.000 1787.842    0.000 {built-in method conv2d}
                2376200 1019.956    0.000 1741.674    0.001 agent.py:59(modify)
                2376200  812.273    0.000 1718.390    0.001 replaybuffer.py:23(sample_data)
               30889310   65.433    0.000 1479.578    0.000 linear.py:93(forward)
               30889310   27.629    0.000 1385.723    0.000 functional.py:1737(linear)
              237620000  298.008    0.000 1361.112    0.000 layers.py:223(isFree)
               30889310 1352.064    0.000 1352.064    0.000 {built-in method torch._C._nn.linear}
                2376200   36.893    0.000 1095.968    0.000 agent.py:96(__call__)
             1486274013  870.539    0.000 1063.103    0.000 layer.py:63(isFree)
                7128170   46.525    0.000 1040.922    0.000 agent.py:54(modify_board)
               19009170  916.392    0.000  916.392    0.000 {built-in method cat}
               85543200  871.600    0.000  871.600    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              237620000  516.778    0.000  849.105    0.000 layers.py:124(check)
               42769880   35.215    0.000  836.813    0.000 activation.py:713(forward)
               42769880   38.998    0.000  801.598    0.000 functional.py:1364(leaky_relu)
               85543200  780.982    0.000  780.982    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1258707   12.409    0.000  778.599    0.001 layers.py:233(restart)
               42769880  755.201    0.000  755.201    0.000 {built-in method torch._C._nn.leaky_relu}
               10053162  754.721    0.000  754.721    0.000 {built-in method tensor}
               19009608  290.224    0.000  742.126    0.000 layer.py:90(update)
                2376200   45.599    0.000  741.008    0.000 replaybuffer.py:19(stacker)
                4752400  115.653    0.000  701.478    0.000 optimizer.py:189(zero_grad)
                7128170  666.815    0.000  666.815    0.000 {built-in method torch._C._nn.one_hot}
                1258707    2.443    0.000  661.990    0.001 levels.py:8(__init__)
                1258707    9.554    0.000  659.546    0.001 level.py:8(__init__)
                1716645   98.873    0.000  632.047    0.000 levels.py:11(generate)
              237620100   63.540    0.000  593.696    0.000 {built-in method builtins.all}
                4752400    5.704    0.000  590.022    0.000 game.py:17(board)
              722215734  163.792    0.000  556.031    0.000 layers.py:197(<genexpr>)
             2027709245  361.079    0.000  517.602    0.000 enum.py:646(__hash__)
                2376200  294.576    0.000  488.501    0.000 collector.py:37(collect)
               42771600  488.331    0.000  488.331    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              154034400  487.120    0.000  487.120    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               42771600  423.557    0.000  423.557    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42771600  403.881    0.000  403.881    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              237620000  255.421    0.000  402.571    0.000 layers.py:95(check)
               42771600  397.872    0.000  397.872    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              237620100  245.232    0.000  370.254    0.000 layers.py:65(isDone)
                4751970  132.973    0.000  361.809    0.000 exploration.py:53(softmaxer)
              655512431  336.430    0.000  336.430    0.000 layer.py:85(elements)
               42771600  317.936    0.000  317.936    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             3654972988  316.316    0.000  316.316    0.000 layer.py:59(positions)
              237620000  208.397    0.000  308.953    0.000 layers.py:50(check)
              237620000  197.611    0.000  303.339    0.000 layers.py:77(check)
              299401254  213.384    0.000  262.451    0.000 tensor.py:906(grad)
                4752400    6.523    0.000  236.231    0.000 loss.py:527(forward)
                4752400   18.297    0.000  229.708    0.000 functional.py:2898(mse_loss)
                1716645  114.249    0.000  216.311    0.000 levels.py:76(RFS)
               14257200  205.071    0.000  205.071    0.000 {built-in method sum}
                7068197   74.941    0.000  193.660    0.000 random.py:315(sample)
              309371380  122.531    0.000  163.997    0.000 layer.py:76(add)
              237515761  108.426    0.000  157.503    0.000 layer.py:72(remove)
             2027726708  156.526    0.000  156.526    0.000 {built-in method builtins.hash}
                3776121   20.254    0.000  151.756    0.000 level.py:41(notUsed)
                4752400  151.337    0.000  151.337    0.000 {built-in method torch._C._nn.mse_loss}
               23761140   17.312    0.000  142.060    0.000 flatten.py:39(forward)
                4753112  135.567    0.000  135.567    0.000 {built-in method max}
                7128600   10.684    0.000  131.717    0.000 tensor.py:525(__rsub__)
        713397549/713397547   91.542    0.000  128.957    0.000 {built-in method builtins.len}
               23761140  124.748    0.000  124.748    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1303662719  124.030    0.000  124.030    0.000 layer.py:125(isBlocking)
                7128600  119.223    0.000  119.223    0.000 {built-in method rsub}
                4751970  115.752    0.000  115.752    0.000 {built-in method multinomial}
              152072160  111.302    0.000  111.302    0.000 {built-in method torch._C._get_tracing_state}
                2376200    9.197    0.000  110.874    0.000 exploration.py:47(epsilonGreedy)
              125760573  106.517    0.000  106.517    0.000 level.py:32(inverse)
                4752400  105.137    0.000  105.137    0.000 {built-in method gather}
                9504800   22.308    0.000  102.406    0.000 profiler.py:615(__enter__)
                4752400   18.694    0.000  101.861    0.000 __init__.py:28(_make_grads)
               10069656   13.712    0.000  100.814    0.000 layer.py:40(restart)
              159993174   67.543    0.000   98.316    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9395482: <9x9_gamme0.95_0> in cluster <dcc> Done

Job <9x9_gamme0.95_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:58 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 01:19:57 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:19:57 2021
Terminated at Tue Mar  9 11:15:26 2021
Results reported at Tue Mar  9 11:15:26 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35589.50 sec.
    Max Memory :                                 5702 MB
    Average Memory :                             4112.46 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2490.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35729 sec.
    Turnaround time :                            36028 sec.

The output (if any) is above this job summary.

